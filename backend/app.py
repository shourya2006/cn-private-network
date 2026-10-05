import argparse
import hashlib
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

parser = argparse.ArgumentParser()
parser.add_argument("--name", choices=("A", "B"), required=True)
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()

CACHE_BODY = json.dumps(
    {"message": "Phase 1 cache resource", "version": 1},
    sort_keys=True,
    separators=(",", ":"),
).encode()
ETAG = '"' + hashlib.sha256(CACHE_BODY).hexdigest() + '"'


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def respond(self, status, body=b"", cache=False):
        self.send_response(status)
        self.send_header("X-Backend", args.name)
        self.send_header(
            "Cache-Control",
            "public, max-age=60" if cache else "no-store",
        )
        if cache:
            self.send_header("ETag", ETAG)
        if status != 304:
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True
        if self.command != "HEAD" and status != 304:
            self.wfile.write(body)

    def handle_request(self):
        path = urlsplit(self.path).path
        if path == "/cache":
            validators = self.headers.get("If-None-Match", "").split(",")
            matches = any(
                value.strip() == "*"
                or value.strip().removeprefix("W/") == ETAG
                for value in validators
            )
            self.respond(304 if matches else 200, CACHE_BODY, cache=True)
            return

        if path in ("/", "/api/status"):
            body = json.dumps(
                {"backend": args.name, "status": "ok"}
            ).encode()
            self.respond(200, body)
            return

        self.respond(404, b'{"error":"Not found"}')

    def do_GET(self):
        self.handle_request()

    def do_HEAD(self):
        self.handle_request()


server = ThreadingHTTPServer(("0.0.0.0", args.port), Handler)
print(
    f"Backend {args.name} listening on 0.0.0.0:{args.port}",
    flush=True,
)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
