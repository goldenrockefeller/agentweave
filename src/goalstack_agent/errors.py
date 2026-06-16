class GoalStackAgentError(Exception):
    pass


class CapabilityError(GoalStackAgentError):
    pass


class MissingFactsError(CapabilityError):
    pass


class CapabilityExecutionError(CapabilityError):
    pass


class BenchmarkError(GoalStackAgentError):
    pass


class AssemblyError(GoalStackAgentError):
    pass
