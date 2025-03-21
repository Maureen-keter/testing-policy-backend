from models import Policy, db
from flask import jsonify, request, make_response
from flask_restful import Resource


class Policies(Resource):
    def get(self):
        # Fetch all policies
        policies_list = []
        for policy in Policy.query.all():
            policy_dict = {
                "id": policy.id,
                "policy_name": policy.policy_name,
                "policy_holder": policy.policy_holder,
                "premium_amount": policy.premium_amount,
                "start_date": policy.start_date,
                "end_date": policy.end_date,
            }
            policies_list.append(policy_dict)
        return make_response(jsonify(policies_list), 200)
    

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
                "policy_name": policy.policy_name,
                "policy_holder": policy.policy_holder,
                "premium_amount": policy.premium_amount,
                "start_date": policy.start_date,
                "end_date": policy.end_date,
            }
            policies_list.append(policy_dict)
        return make_response(jsonify(policies_list), 200)

    def post(self):
        # Add a new policy
        data = request.get_json()
        try:
            new_policy = Policy(
                policy_name=data["policy_name"],
                policy_holder=data["policy_holder"],
                premium_amount=data["premium_amount"],
                start_date=data["start_date"],
                end_date=data["end_date"],
            )
            db.session.add(new_policy)
            db.session.commit()
            return make_response(jsonify(["Policy added successfully"]), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": str(e)}), 400)

