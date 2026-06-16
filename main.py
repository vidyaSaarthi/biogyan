from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change to your actual website domain
    allow_methods=["POST"],
    allow_headers=["*"],
)


# Define the data structure we expect from the frontend
class Lead(BaseModel):
    whatsapp_number: str


@app.post("/api/lead")
async def capture_lead(lead: Lead):
    phone_number = lead.whatsapp_number

    # 1. Validation: Ensure it's not empty
    if not phone_number:
        raise HTTPException(status_code=400, detail="WhatsApp number is required")

    try:
        # ---------------------------------------------------------
        # TO DO:
        # Insert your logic here to save 'phone_number'
        # into your Counselling Tracker (e.g., via Google Sheets API,
        # PostgreSQL, or a CRM webhook)
        # ---------------------------------------------------------
        print(f"New Lead Captured for Counselling Tracker: {phone_number}")

        # ---------------------------------------------------------
        # TO DO:
        # Trigger WhatsApp Business API here to send the Zoom link
        # instantly to the student.
        # ---------------------------------------------------------

        return {"status": "success", "message": "Lead saved and WhatsApp message triggered."}

    except Exception as e:
        print(f"Database/API Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run this using the command: uvicorn main:app --reload