from scholarly import ProxyGenerator, scholarly
import json
import os
from datetime import datetime, timezone


class CitationDataUnavailable(RuntimeError):
    """Raised when Google Scholar returns an incomplete author profile."""


def configure_proxy() -> None:
    """Optionally route Scholar traffic through a user-provided proxy."""
    proxy_url = os.getenv("GOOGLE_SCHOLAR_PROXY")
    if not proxy_url:
        return

    proxy = ProxyGenerator()
    if not proxy.SingleProxy(http=proxy_url, https=proxy_url):
        raise RuntimeError("GOOGLE_SCHOLAR_PROXY could not be configured.")
    scholarly.use_proxy(proxy, proxy)


def citation_total(author: dict) -> int:
    """Return Google Scholar's total citations with a yearly-count fallback."""
    citedby = author.get("citedby")
    if citedby is not None:
        return int(citedby)

    cites_per_year = author.get("cites_per_year")
    if isinstance(cites_per_year, dict) and cites_per_year:
        try:
            total = sum(int(count) for count in cites_per_year.values())
        except (TypeError, ValueError) as error:
            raise CitationDataUnavailable(
                "Google Scholar returned invalid values in cites_per_year."
            ) from error

        print("Google Scholar omitted 'citedby'; derived it from cites_per_year.")
        return total

    available_fields = ", ".join(sorted(author.keys()))
    raise CitationDataUnavailable(
        "Google Scholar returned neither 'citedby' nor usable 'cites_per_year'. "
        "This is usually caused by rate limiting, a CAPTCHA, or a changed "
        f"Scholar response. Available fields: {available_fields}"
    )


def fetch_author() -> dict:
    scholar_id = os.getenv("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is not configured.")

    configure_proxy()
    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
    )

    if "publications" not in author:
        raise CitationDataUnavailable(
            "Google Scholar returned an incomplete profile without publications."
        )

    author["citedby"] = citation_total(author)
    return author


def main() -> None:
    author = fetch_author()
    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        publication["author_pub_id"]: publication for publication in author["publications"]
    }
    print(json.dumps(author, indent=2))
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
