"""Preview Flepsite locally without caching pages or assets."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    handler = partial(PreviewHandler, directory=str(root))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Flepsite preview: http://localhost:{args.port}/ (caching disabled)", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
