# GCE
GCE — Geometric Combinatorial Encryption


GCE (Geometric Combinatorial Encryption) is an experimental encryption framework based on structural encoding, hidden grids, combinatorial masking, and reversible distortions.

Instead of encoding data as symbols or numbers, GCE represents information as geometric or combinatorial structures embedded within a large and obfuscated point space.

---

## 🧠 Core Idea

GCE operates in three main layers:

1. **Structural Encoding**  
   Messages are encoded as binary structures on a discrete grid using a shared rule system.

2. **Combinatorial Masking**  
   The meaningful structure is embedded בתוך a large set of extraneous points, creating a vast search space.

3. **Reversible Distortion**  
   Global transformations are applied to all points, removing any explicit trace of the grid and encoding structure.

The result is a dataset where:
- The grid is not directly visible  
- The message structure is hidden  
- No clear starting point exists without prior knowledge  

---

## 🤝 Handshake (Initialization)

Before communication, a one-time handshake defines the shared rule system:

- Binary encoding rule  
- Verifier (anchor for grid reconstruction)  
- Termination rule  
- Distortion functions  
- Combinatorial modification rules  

After initialization, all messages follow the same rules.

---

## 🔍 Decoding Overview

Decoding requires knowledge of the handshake and consists of:

1. Applying inverse transformations  
2. Locating the verifier (anchor)  
3. Reconstructing the hidden grid  
4. Identifying valid structures  
5. Interpreting them using the binary rule  

---

## ⚙️ Example Implementation

This repository includes a Python reference implementation demonstrating one possible instantiation of the framework (using simple geometric constructions).

> Note: The geometric shapes used in the implementation (e.g., triangles) are only one example and do not limit the general framework.

---

## 🚀 Features

- One-time initialization (handshake)
- Flexible structural encoding (not limited to fixed formats)
- High-dimensional embedding
- Combinatorial obfuscation
- Reversible distortion layer
- Support for decoy structures and noise injection
- Extensible rule-based design

---

This project implements the GCE (Geometric Combinatorial Encryption) scheme. For the full theoretical background and formal description, please refer to the paper: A Geometric-Combinatorial Encryption Scheme Based on Structural Rules and Obfuscated Embedding

Link: https://zenodo.org/records/19670590

## ⚠️ Disclaimer

This project is experimental.

It is **not a formally verified cryptographic system**, and no security guarantees are provided. 

