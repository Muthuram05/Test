from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/result', methods=['GET'])
def login():
    return jsonify({
    "_id": "Fpm93MJWO1U7w",
    "ConversationId": "Cn93MJWO1U7w",
    "Assistant": "To ensure I understand your needs correctly for creating a medical reimbursement request, could you please confirm the primary requirement of your request by choosing one of the following options?\n\n1. Do you need a way to visualize and manage tasks related to medical reimbursement requests, including assigning tasks and tracking progress without strict approval cycles?\n2. Are you looking for a system to manage structured approval workflow cycles for medical reimbursement requests, with predefined steps and decision-making criteria?\n3. Do you require a custom application that combines data management, integrations, and possibly includes workflow automation for handling medical reimbursement requests?\n\nPlease select the number that best matches your needs.",
    "Suggestion": False
})

@app.route('/suggestion', methods=['GET'])
def search(): 
    return jsonify({
    "_id": "Fpm93MJWO1U7w",
    "ConversationId": "Cn93MJWO1U7w",
    "Assistant": {
        "FlowType": "Board",
        "FlowAccess": True,
        "FlowName": "Medical Reimbursement Requests",
        "ItemType": "Request",
        "Prefix": "MR",
        "Description": "A board to track and manage medical reimbursement requests submitted by employees. Allows for easy visualization of request statuses and facilitates communication between team members.",
        "Reasoning": {
            "ReasonForPickingThisFlow": "The Board module is chosen because it provides a flexible way to track and manage medical reimbursement requests without the need for a strict approval process. It supports visualizing workflows, allocating tasks, and monitoring progress efficiently, which aligns with the need to manage these requests in a dynamic and collaborative environment.",
            "ReasonForNotPickingOtherFlows": "The Process module was not selected because it focuses on structured approval workflow cycles, which is more than what's needed for this scenario. The Apps module, while powerful for creating custom applications, is not necessary for the straightforward task of tracking and managing reimbursement requests.",
        }
    },
    "Suggestion": True
})

if __name__ == '__main__':
    app.run(debug=True)