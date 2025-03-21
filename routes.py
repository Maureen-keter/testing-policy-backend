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
