import asyncio
from app.core.email import send_verification_email

async def test():
    try:
        await send_verification_email(
            ["mahligautam83@gmail.com"],  # Change to your email
            "Test User",
            "test-token-123"
        )
        print("✓ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())