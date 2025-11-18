# agent-doc-ex

Overview
--------
A Python project for testing and demonstrating LandingAI's agentic document extraction capabilities. This project includes mupltiple implementations, including the LandingAI ADE Python library, their legacy agentic-doc library, and vanilla API requests.


Project Setup
--------
1. Regist for a LandingAI account and generate a personal API key

2. Clone the repository and navigate to the project directory

3. Create a `secrets.toml` file in the project root with your API credentials:
   ```toml
   VISION_AGENT_API_KEY = "your-api-key-here"
   ```


Usage
--------
Place your documents in the `Test/` directory, then run one of the implementation to: 
- Process all documents in the `Test/` directory
- Convert them to Markdown format
- Save the output with the same filename but `.md` extension
- Print processing status and any errors encountered


Helpful Resources
--------
- [LandingAI ADE API Documentation](https://docs.landing.ai/api-reference/tools/ade-parse)
- [LandingAI ADE Python Library](https://github.com/landing-ai/ade-python)
- [Agentic Doc Library](https://github.com/landing-ai/agentic-doc/)
- [Supported File Types](https://docs.landing.ai/ade/ade-file-types)
