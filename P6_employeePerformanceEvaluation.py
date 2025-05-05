# Knowledge Base
positive_criteria = {
    "exceeds_deadlines": 5,
    "high_quality_work": 4,
    "great_team_player": 3,
    "consistently_improves": 2,
    "excellent_communication": 1
}

negative_criteria = {
    "misses_deadlines": -5,
    "poor_quality_work": -4,
    "poor_team_player": -3,
    "resistant_to_feedback": -2,
    "poor_communication": -1
}

# Rule Engine
def evaluate_employee(positives, negatives):
    score = 0
    for pos in positives:
        score += positive_criteria.get(pos, 0)
    for neg in negatives:
        score += negative_criteria.get(neg, 0)
    return score

# User Interface
def user_interface():
    print("=== Employee Performance Evaluation ===\n")

    print("Please enter positive criteria from the list below, separated by commas:")
    for criterion in positive_criteria:
        print(f"- {criterion}")

    positives_input = input("\nEnter positive criteria: ")
    
    print("\nPlease enter negative criteria from the list below, separated by commas:")
    for criterion in negative_criteria:
        print(f"- {criterion}")
        
    negatives_input = input("\nEnter negative criteria: ")

    # Clean and parse input
    positives = [item.strip() for item in positives_input.split(",") if item.strip()]
    negatives = [item.strip() for item in negatives_input.split(",") if item.strip()]

    # Calculate score
    score = evaluate_employee(positives, negatives)

    # Output result
    print(f"\nEmployee Score: {score}")
    if score > 10:
        print("Performance: Outstanding")
    elif score > 5:
        print("Performance: Good")
    elif score > 0:
        print("Performance: Satisfactory")
    else:
        print("Performance: Needs Improvement")

# Run the program
if __name__ == "__main__":
    user_interface()

# 1. **What is an Expert System?**
# An Expert System is a computer system designed to mimic the decision-making abilities of a human expert in solving complex problems. 
# #It uses a knowledge base and inference rules to simulate human expertise in specific domains, like medical diagnosis, troubleshooting, etc.

# 2. **What are the components of an Expert System?**
# An Expert System typically consists of four main components:
#   - **Knowledge Base:** This stores the facts, rules, and data relevant to the problem domain.
#   - **Inference Engine:** It processes the knowledge in the knowledge base to derive conclusions or make decisions.
#   - **User Interface:** The part of the system that allows interaction with the user to input queries and display results.
#   - **Explanation Facility:** This component provides explanations to users about how conclusions are reached.

# 3. **What is the role of the knowledge base in an Expert System?**
# The knowledge base serves as the core of an Expert System. It stores all the information, facts, and rules related to the domain of expertise. This knowledge is then used by the inference engine to make decisions or provide recommendations.

# 4. **What is the difference between an Expert System and a traditional program?**
# Traditional programs follow a predefined sequence of instructions, while Expert Systems use reasoning and rules to make decisions based on a set of facts. Expert Systems can handle uncertain or incomplete information and simulate the decision-making of a human expert.

# 5. **What is the inference engine and how does it work?**
# The inference engine is the "brain" of the Expert System. It applies logical rules to the knowledge base and derives conclusions based on user inputs. It uses two types of reasoning:
#   - **Forward Chaining:** Starting with known facts and applying rules to infer new facts.
#   - **Backward Chaining:** Starting with a goal and working backward to find the facts that support the goal.

# 6. **What is forward chaining in Expert Systems?**
# Forward chaining is a method of reasoning where the inference engine starts with the available facts and applies rules to infer new facts. This process continues until a goal is achieved or no further conclusions can be made.

# 7. **What is backward chaining in Expert Systems?**
# Backward chaining is a goal-driven reasoning approach. The inference engine starts with a goal and works backward, asking whether certain facts are true to support the goal. It tries to prove the goal by finding facts and rules that lead to it.

# 8. **Can an Expert System handle uncertain information?**
# Yes, some Expert Systems can handle uncertain information using techniques like fuzzy logic or probabilistic reasoning. These techniques allow the system to make decisions based on incomplete or ambiguous data, which is common in real-world scenarios.

# 9. **What are the advantages of Expert Systems?**
#   - **Consistency:** They provide consistent decision-making by following the same set of rules.
#   - **Availability:** Expert Systems are available 24/7 and can provide answers or solutions at any time.
#   - **Efficiency:** They can process large amounts of data quickly and make complex decisions in real-time.
#   - **No Human Error:** They eliminate human errors in decision-making as they follow strict logic and rules.

# 10. **What are the limitations of Expert Systems?**
#   - **Lack of Flexibility:** Expert Systems are domain-specific and cannot adapt to new or unforeseen situations outside their programmed knowledge base.
#   - **Maintenance:** Updating the knowledge base to accommodate new information requires human intervention and can be time-consuming.
#   - **Cost:** Developing and maintaining Expert Systems can be expensive, especially when they are applied to complex domains.

# 11. **What are some real-world applications of Expert Systems?**
# Expert Systems are widely used in various fields such as:
#   - **Medical Diagnosis:** Expert Systems like MYCIN help doctors diagnose diseases based on symptoms and test results.
#   - **Troubleshooting and Repair:** Expert Systems in technical support can help troubleshoot equipment or software issues.
#   - **Financial Planning:** Expert Systems help financial advisors assess investment risks and make portfolio recommendations.
#   - **Legal Advice:** Some Expert Systems provide legal recommendations based on current laws and precedents.

# 12. **What is fuzzy logic in Expert Systems?**
# Fuzzy logic is a form of reasoning that allows for uncertainty or partial truth, unlike traditional binary logic. It is used in Expert Systems to handle vague or imprecise data. For example, rather than classifying something as "hot" or "cold," fuzzy logic might classify it as "somewhat hot," allowing for more nuanced decision-making.

# 13. **What is the difference between rule-based systems and case-based reasoning in Expert Systems?**
# Rule-based systems use a set of predefined rules to make decisions, while case-based reasoning (CBR) relies on past experiences (cases) to solve new problems. In CBR, the system retrieves similar past cases, adapts them to the current situation, and suggests a solution based on these cases.

# 14. **What are some challenges in developing Expert Systems?**
#   - **Knowledge Acquisition:** Gathering the necessary domain knowledge can be difficult, especially in complex areas where expert knowledge is scarce or hard to articulate.
#   - **Knowledge Representation:** Choosing the appropriate format to represent knowledge effectively can be a challenge, especially in dynamic environments.
#   - **Scalability:** As the knowledge base grows, it becomes harder to maintain and optimize the Expert System for performance.

# 15. **What are hybrid Expert Systems?**
# Hybrid Expert Systems combine multiple AI techniques, such as rule-based reasoning, fuzzy logic, neural networks, and genetic algorithms, to improve decision-making capabilities. These systems can handle a wider range of problems and provide more accurate and reliable solutions.
