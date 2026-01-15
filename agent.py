# agent.py

from tools import send_whatsapp_message, ToolError


def run_agent(input_data: dict) -> dict:
    if "contact_name" not in input_data or "message" not in input_data:
        return {"status": "DONE", "result": "Bad input"}

    try:
        result = send_whatsapp_message(
            input_data["contact_name"],
            input_data["message"]
        )
    except ToolError as e:
        return {"status": "DONE", "result": f"Failed: {e}"}

    return {"status": "DONE", "result": result["detail"]}


if __name__ == "__main__":
    contact_name = input("Enter contact name: ")
    message = input("Enter message: ")

    output = run_agent({
        "contact_name": contact_name,
        "message": message
    })

    print(output)
