from openai import OpenAI
from config import Config
import base64
from io import BytesIO

class AnswerGenerator:
    """Generates answers to interview questions using OpenAI API"""
    
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL
        self.system_prompt = Config.SYSTEM_PROMPT
        self.client = None
        self.conversation_history = []
        
    def initialize(self):
        """Initialize OpenAI client"""
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in .env file")
        
        self.client = OpenAI(api_key=self.api_key)
        print("Answer generator initialized")
        
    def generate_answer(self, question, context=None, screenshot=None):
        """
        Generate an answer to the interview question
        
        Args:
            question: The interview question text
            context: Optional additional context or previous conversation
            screenshot: Optional PIL Image object of screen capture
            
        Returns:
            str: Generated answer
        """
        if not self.client:
            self.initialize()
            
        if not question or question.strip() == "":
            return ""
        
        try:
            # Build messages
            messages = [
                {"role": "system", "content": self.system_prompt}
            ]
            
            # Add context if provided
            if context:
                messages.append({
                    "role": "system",
                    "content": f"Additional context: {context}"
                })
            
            # Add conversation history (last 3 exchanges)
            messages.extend(self.conversation_history[-6:])
            
            # Prepare user message content
            user_content = [{"type": "text", "text": f"Interview question: {question}"}]
            
            # Add screenshot if provided (for vision model)
            if screenshot and "gpt-4" in self.model:
                try:
                    # Convert PIL Image to base64
                    buffered = BytesIO()
                    screenshot.save(buffered, format="PNG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode()
                    
                    user_content.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{img_base64}",
                            "detail": "low"  # Use 'low' for cost efficiency
                        }
                    })
                except Exception as e:
                    print(f"Warning: Could not process screenshot: {e}")
            
            # Add current question
            messages.append({
                "role": "user",
                "content": user_content if screenshot and "gpt-4" in self.model else f"Interview question: {question}"
            })
            
            # Generate response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            answer = response.choices[0].message.content.strip()
            
            # Update conversation history
            self.conversation_history.append({
                "role": "user",
                "content": question
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": answer
            })
            
            return answer
            
        except Exception as e:
            print(f"Error generating answer: {e}")
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        
    def set_context(self, context):
        """Set additional context for answer generation"""
        self.context = context
