from models import Policy, db
from flask import jsonify, request, make_response
from flask_restful import Resource


# Resource for handling all policies
class Policies(Resource):
    def get(self):
        # Fetch all policies
        policies_list = []
        for policy in Policy.query.all():
            policy_dict = {
                "id": policy.id,
                "name": policy.name,
                "type": policy.type,
                "premium": policy.premium,
                "status": policy.status,
            }
            policies_list.append(policy_dict)
        return make_response(jsonify(policies_list), 200)

    def post(self):
        # Add a new policy
        data = request.get_json()
        try:
            new_policy = Policy(
                name=data["name"],
                type=data["type"],
                premium=data["premium"],
                status=data.get("status", "active"),  # Default to "active" if not provided
            )
            db.session.add(new_policy)
            db.session.commit()
            return make_response(jsonify({"message": "Policy added successfully"}), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": str(e)}), 400)


# Resource for handling a single policy by ID
class PolicyByID(Resource):
    def get(self, id):
        # Fetch a policy by ID
        policy = Policy.query.filter_by(id=id).first()
        if not policy:
            return make_response(jsonify({"error": "Policy not found"}), 404)

        policy_dict = {
            "id": policy.id,
            "name": policy.name,
            "type": policy.type,
            "premium": policy.premium,
            "status": policy.status,
        }
        return make_response(jsonify(policy_dict), 200)

    def patch(self, id):
        # Update a policy
        policy = Policy.query.filter_by(id=id).first()
        if not policy:
            return make_response(jsonify({"error": "Policy not found"}), 404)

        data = request.json
        for field in ["name", "type", "premium", "status"]:
            if field in data:
                setattr(policy, field, data[field])

        db.session.commit()
        return make_response(jsonify({"message": "Policy updated successfully"}), 200)

    def delete(self, id):
        # Delete a policy
        policy = Policy.query.filter_by(id=id).first()
        if not policy:
            return make_response(jsonify({"error": "Policy not found"}), 404)

        db.session.delete(policy)
        db.session.commit()
        return make_response(jsonify({"message": "Policy deleted successfully"}), 200)
