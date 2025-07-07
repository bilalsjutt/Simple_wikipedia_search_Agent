# Wikipedia Search Agent

A simple AI agent built with LangChain that can search Wikipedia and maintain conversation memory. The agent uses OpenAI's GPT-3.5-turbo model and follows the ReAct (Reasoning and Acting) pattern to answer questions by searching Wikipedia when needed.

## Features

- **Wikipedia Search**: Searches Wikipedia using the REST API for information
- **Conversation Memory**: Remembers previous conversations using ConversationBufferMemory
- **ReAct Pattern**: Uses reasoning and action loops to determine when to search
- **Error Handling**: Gracefully handles API errors and exceptions
- **Logging**: Comprehensive logging for debugging and monitoring

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd wikipedia-search-agent
```

2. Install required dependencies:
```bash
pip install langchain-openai langchain python-dotenv requests
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the script:
```bash
python main.py
```

The agent will process the default query about the 2022 FIFA World Cup winner. You can modify the input in the script to ask different questions.

### Example Usage

```python
# Modify the last line to ask different questions
response = executor.invoke({"input": "Tell me about the Eiffel Tower"})
print(response['output'])
```

## How It Works

1. **Wikipedia Tool**: The `Wiki_search` function queries Wikipedia's REST API to retrieve page summaries
2. **LLM Setup**: Uses OpenAI's GPT-3.5-turbo model with temperature=0 for consistent responses
3. **Memory**: Maintains conversation history using ConversationBufferMemory
4. **ReAct Agent**: Follows the ReAct pattern to reason about when to use tools
5. **Agent Executor**: Orchestrates the agent's decision-making process

## Project Structure

```
.
├── main.py              # Main application file
├── .env                 # Environment variables (create this)
├── README.md           # This file
└── requirements.txt    # Dependencies (optional)
```

## API Response Format

The agent returns responses in the following format:
```python
{
    'input': 'Your question',
    'output': 'Agent response',
    'chat_history': [...],  # Previous conversation
    'intermediate_steps': [...]  # Agent's reasoning steps
}
```

## Error Handling

The application includes error handling for:
- Wikipedia API failures
- Network connectivity issues
- Invalid search queries
- OpenAI API errors

## Customization

### Adding New Tools

To add more tools, create a new function and Tool instance:

```python
def new_tool_function(query):
    # Your tool logic here
    return result

new_tool = Tool(
    name="NewTool",
    func=new_tool_function,
    description="Description of what this tool does"
)

# Add to tools list
tools = [tool, new_tool]
```

### Modifying the Prompt

You can customize the agent's behavior by modifying the `template` variable to change how the agent reasons and responds.

## Dependencies

- `langchain-openai`: OpenAI integration for LangChain
- `langchain`: Core LangChain functionality
- `python-dotenv`: Environment variable management
- `requests`: HTTP requests for Wikipedia API

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

**Common Issues:**

- **API Key Error**: Make sure your OpenAI API key is correctly set in the `.env` file
- **Wikipedia Search Fails**: Check your internet connection and verify the Wikipedia API is accessible
- **Import Errors**: Ensure all dependencies are installed with the correct versions

**Debug Mode:**
The application includes logging. Check the console output for detailed error messages and execution flow.

## Future Enhancements

- Add more search sources (Google, Bing, etc.)
- Implement caching for repeated queries
- Add a web interface using Streamlit or Flask
- Support for multiple languages
- Add unit tests and CI/CD pipeline
