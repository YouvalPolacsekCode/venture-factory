"""Product Hunt source fetcher — placeholder until a PH API key is provisioned.

PH requires an authenticated GraphQL API. Until that's enabled via a
`register_external_account` approval, this raises so the source is never
silently treated as empty when someone flips `enabled: true` prematurely."""


def fetch(source_config: dict) -> list[dict]:
    if not source_config.get("enabled"):
        return []
    raise NotImplementedError(
        "Product Hunt fetcher not implemented. Provision a PH API key and "
        "implement GraphQL fetch before enabling this source."
    )
