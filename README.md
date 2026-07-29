# Opera Neon Spatial Workspace — 3D Spatial Window Manager 🌐

> **Spatial workspace layout manager and window position synthesizer for 3D browser interfaces.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue)]()
[![Domain](https://img.shields.io/badge/Domain-Spatial%20UI-purple)]()

---

## 🎯 For Recruiters & Hiring Managers

This repository implements the **Opera Neon Spatial Workspace Manager** — computing 3D spatial layout coordinates, window depth layers, and physics-based window positioning for immersive browser interfaces. It demonstrates:

- **3D spatial grid calculations** arranging browser windows in 3D coordinate space
- **Depth-based focus scaling** applying parallax and scale transformations to inactive windows
- **Physics-based window positioning** simulating momentum and spring physics during tab drag operations
- **Python state manager** storing and restoring spatial workspace layouts deterministically

**Why this matters**: As spatial computing (VisionOS, WebXR) matures, traditional 2D window managers are giving way to 3D spatial layout engines.

---

## 🔬 For Engineers & Technical Reviewers

### Core Components

| Component | Language | Purpose |
|---|---|---|
| `src/spatial_workspace.py` | Python | Spatial 3D coordinate solver and layout manager |
| `tests/` | Python | Test suite for 3D layout math and window focus transitions |

---

## 🤖 ML/AI & Programmatic Mesh Integration

- **MCP Tool**: `arrange_spatial_windows()` — tool for spatial agent layout generation
- **Mastermind Sidecar**: Connected to APEX Highway mesh
- **SHA-256 Integrity**: Tracked in `.integrity/file_hashes.json`

---

## ⚡ Quick Start

```bash
python3 src/spatial_workspace.py
```
