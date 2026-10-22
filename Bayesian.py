#python -m pip install pgmpy


from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define network structure: Study -> ExamResult
model = DiscreteBayesianNetwork([
    ('Study', 'ExamResult')
])

# Define CPD for Study
cpd_study = TabularCPD(
    variable='Study',
    variable_card=2,
    values=[[0.6], [0.4]]
)
# 0: Did not study, 1: Studied

# Define CPD for ExamResult
cpd_exam = TabularCPD(
    variable='ExamResult',
    variable_card=2,
    values=[
        [0.8, 0.2],  # P(Fail | Study)
        [0.2, 0.8]   # P(Pass | Study)
    ],
    evidence=['Study'],
    evidence_card=[2]
)

# Add CPDs to model
model.add_cpds(cpd_study, cpd_exam)

# Validate model
model.check_model()

# Perform inference
inference = VariableElimination(model)

# Probability of passing given that the student studied
result = inference.query(
    variables=['ExamResult'],
    evidence={'Study': 1}
)

print(result)
