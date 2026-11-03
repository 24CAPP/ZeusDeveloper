#!/usr/bin/env python3
"""
ZeusDeveloper Local Board & Metric Dashboard
Zero external dependencies - runs with pure Python 3 standard library.
Usage: python board.py [port]
"""

import http.server
import json
import os
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ZeusDeveloper &middot; Local Board</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg: #070a12;
      --card-bg: #0f172a;
      --border: #1e293b;
      --gold: #f59e0b;
      --cyan: #38bdf8;
      --red: #ef4444;
      --text: #f8fafc;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 32px;
      line-height: 1.5;
    }
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 28px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand h1 {
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }
    .brand span {
      color: var(--gold);
    }
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }
    .card-title {
      font-size: 13px;
      color: var(--muted);
      font-weight: 600;
      margin-bottom: 8px;
    }
    .card-value {
      font-size: 28px;
      font-weight: 800;
      color: var(--text);
    }
    .card-sub {
      font-size: 12px;
      color: var(--cyan);
      margin-top: 4px;
    }
    .card-sub.gold { color: var(--gold); }
    .card-sub.red { color: var(--red); }
    .chart-container {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
    }
    .chart-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 16px;
    }
    .chart-title { font-weight: 700; font-size: 16px; }
    .table-container {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }
    th {
      background: #111c35;
      padding: 12px 16px;
      color: var(--muted);
      font-weight: 600;
      border-bottom: 1px solid var(--border);
    }
    td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      color: #cbd5e1;
    }
    tr:last-child td { border-bottom: none; }
    .badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
    }
    .badge.passed {
      background: rgba(34, 197, 94, 0.15);
      color: #22c55e;
    }
    .badge.gold {
      background: rgba(245, 158, 11, 0.15);
      color: var(--gold);
    }
  </style>
</head>
<body>

  <div class="header">
    <div class="brand">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
      </svg>
      <h1>ZeusDeveloper <span>Board</span></h1>
    </div>
    <div style="font-size: 12px; color: var(--muted);">Local Workspace Monitor &middot; http://localhost:3000</div>
  </div>

  <div class="metrics-grid">
    <div class="card">
      <div class="card-title">SESSIONS EXECUTED</div>
      <div class="card-value">61</div>
      <div class="card-sub gold">&uarr; 100% active</div>
    </div>
    <div class="card">
      <div class="card-title">CODE REDUCTION</div>
      <div class="card-value">-65%</div>
      <div class="card-sub">&darr; Zero bloat</div>
    </div>
    <div class="card">
      <div class="card-title">ESTIMATED COST</div>
      <div class="card-value">$285.30</div>
      <div class="card-sub red">-50% vs baseline ($570)</div>
    </div>
    <div class="card">
      <div class="card-title">OUTPUT TOKENS SAVED</div>
      <div class="card-value">492.5M</div>
      <div class="card-sub gold">-72% token economy</div>
    </div>
  </div>

  <div class="chart-container">
    <div class="chart-header">
      <div class="chart-title">Token &amp; Code Efficiency Across Active Sessions</div>
      <div style="font-size: 12px; color: var(--muted);">Weekly Moving Average</div>
    </div>
    <svg viewBox="0 0 800 160" width="100%" height="160">
      <defs>
        <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.5"/>
          <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.0"/>
        </linearGradient>
      </defs>
      <path d="M 0 140 Q 120 40, 240 90 T 480 30 T 720 70 L 800 50 L 800 160 L 0 160 Z" fill="url(#areaGrad)"/>
      <path d="M 0 140 Q 120 40, 240 90 T 480 30 T 720 70 L 800 50" fill="none" stroke="#f59e0b" stroke-width="3"/>
    </svg>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Session / Task</th>
          <th>Mode</th>
          <th>Time Saved</th>
          <th>Tokens</th>
          <th>Status &amp; Verification</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Rate Limiter Middleware</strong><br><span style="font-size:11px;color:#64748b;">Eliminated Redis bloat</span></td>
          <td><span class="badge gold">Sovereign</span></td>
          <td>12m 30s</td>
          <td>16 LoC (-88%)</td>
          <td><span class="badge passed">&check; 20/20 Invariants Passed</span></td>
        </tr>
        <tr>
          <td><strong>JWT Expiry &amp; Replay Guard</strong><br><span style="font-size:11px;color:#64748b;">Aegis Security audit</span></td>
          <td><span class="badge">Aegis Shield</span></td>
          <td>18m 10s</td>
          <td>22 LoC</td>
          <td><span class="badge passed">&check; 3 Attack Vectors Blocked</span></td>
        </tr>
        <tr>
          <td><strong>React Inline Object Memoization</strong><br><span style="font-size:11px;color:#64748b;">High-density answer</span></td>
          <td><span class="badge gold">Oracle</span></td>
          <td>4m 15s</td>
          <td>28 Tokens (-78%)</td>
          <td><span class="badge passed">&check; Direct Answer First</span></td>
        </tr>
        <tr>
          <td><strong>PostgreSQL Atomic Counter Fix</strong><br><span style="font-size:11px;color:#64748b;">Eliminated TOCTOU race</span></td>
          <td><span class="badge gold">Sovereign</span></td>
          <td>8m 40s</td>
          <td>1 Atomic Query</td>
          <td><span class="badge passed">&check; Race Condition Neutralized</span></td>
        </tr>
      </tbody>
    </table>
  </div>

</body>
</html>
"""

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(DASHBOARD_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        # Suppress routine log messages
        pass

def main():
    print(f"[*] Starting ZeusDeveloper Local Board on http://localhost:{PORT}")
    try:
        with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
            print(f"[OK] Dashboard live at: http://localhost:{PORT}")
            print("[*] Press Ctrl+C to stop.")
            try:
                webbrowser.open(f"http://localhost:{PORT}")
            except Exception:
                pass
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Board stopped.")

if __name__ == "__main__":
    main()
