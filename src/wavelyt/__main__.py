"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Wavelyt."""


if __name__ == "__main__":
    main(prog_name="wavelyt")  # pragma: no cover
