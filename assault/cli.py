import click

from .http_request import assault


@click.command()
@click.option("--request", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Output JSON file path")
@click.argument("url")
def cli(request, concurrency, json_file, url):
    print(f"Requests: {request}")
    print(f"Concurrency: {concurrency}")
    print(f"JSON-File: {json_file}")
    print(f"Url: {url}")
    assault(url, request, concurrency)


if __name__ == "__main__":
    cli()
