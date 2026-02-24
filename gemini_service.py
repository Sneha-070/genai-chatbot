import google.generativeai as genai
from config import Config
from services.logger_service import log_info, log_error

# Configure Gemini once
genai.configure(api_key=Config.GEMINI_API_KEY)


class GeminiService:

    def __init__(self):
        self.model = genai.GenerativeModel(Config.MODEL_NAME)

    def generate_response(self, system_prompt, chat_history):

        try:
            log_info("Calling Gemini API")

            # Build structured prompt
            full_prompt = system_prompt

            for message in chat_history:
                role = message["role"]
                text = message["parts"][0]
                full_prompt += f"\n{role}: {text}"

            response = self.model.generate_content(full_prompt)

            log_info("Gemini API call successful")

            return response.text

        except Exception as e:
            print("Gemini ERROR:", str(e))  # 👈 Add this line
            log_error(f"Gemini API error: {str(e)}")
            return f"ERROR: {str(e)}"


# ----------------------------------------------------------
# Conversation Summary Function (Used in Sidebar)
# ----------------------------------------------------------

def summarize_conversation(chat_history):
    try:
        log_info("Generating conversation summary")

        model = genai.GenerativeModel(Config.MODEL_NAME)

        conversation_text = ""

        for message in chat_history:
            role = message["role"]
            text = message["parts"][0]
            conversation_text += f"{role}: {text}\n"

        summary_prompt = f"""
        You are a mental health support assistant.

        Provide a short structured summary of the conversation below.
        Focus on:
        - Emotional state
        - Key concerns
        - Main stress triggers
        - Coping suggestions discussed

        Keep it under 150 words.

        Conversation:
        {conversation_text}
        """

        response = model.generate_content(summary_prompt)

        log_info("Summary generated successfully")

        return response.text

    except Exception as e:
        log_error(f"Operation failed: {str(e)}")
        return "An error occurred while processing. Please try again later."