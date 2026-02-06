# Ryuki-AI-Town
![ryuki-advent](https://github.com/user-attachments/assets/8c9f3edd-7ede-49ed-85fa-4f394e686667)
![knight-kamen-rider-knight](https://github.com/user-attachments/assets/52165400-48ab-456f-a8e6-c459e506e93b)

Ryuki-AI-Town: A Multi-Agent Generative Narrative Simulation
Experimental framework for simulating stochastic narrative dynamics and agent persona consistency within a deterministic time-loop.

This project is a LLM-powered multi-agent simulation framework based on Kamen Rider Ryuki. It leverages local inference (via Ollama) and an event-driven architecture to explore emergent character behaviors and alternative story equilibria in a latent narrative space.

## Inspiration & Philosophy:
In the universe of Kamen Rider Ryuki, characters are trapped in an endless cycle of battle. This project aims to "break the loop" by introducing AI-driven agency.

By modeling intricate interpersonal dependencies—such as the complex bond between Kitaoka Shuichi and Yura Goro—we allow the simulation to evolve beyond its original script. Each "Time Vent" in this town isn't a mere reset; it is a new branching path where agent decisions are grounded in their unique psychological profiles.

## Core Features:
1. Decoupled Persona Management
All character data is isolated in structured JSON configurations, allowing for:
High Extensibility: Add new Riders (e.g., Tezuka Miyuki, Asakura Takeshi) without modifying core logic.
2. Local Inference & Privacy
Engine: Ollama (Llama 3:8B)
Parameter Tuning: Balanced temperature (0.8) and presence_penalty (0.5) for creative yet consistent dialogue.
(PS: I tried the qwen models but they seem not work perfectly)

## System Workflow
Initialization: Random "Starter" selection to initiate the cycle.
Context Injection: Dynamic merging of Persona + Event Data + Interaction Rules.
State Transition: Real-time content scanning for keyword-triggered event switching (e.g., from Office Peace to Mirror Monster Attack).

## DEMO response
here is a demo response to show the progress
<img width="1451" height="464" alt="截圖 2026-02-05 21 53 39" src="https://github.com/user-attachments/assets/a47b9387-6e75-4ef9-89e4-10256f6baa93" />

