# SVL 1617 - M. Nebut
# CTD4 - exo service et sessions
# 3 implems qui se sont succedes au fil des questions

# Q1.1
class Sessions1:

    def __init__(self):
        self.current = []

    def add(self, session):
        self.current.append(session)

    def current_sessions(self):
        return self.current

    def kill(self):
        for session in self.current:
            session.kill()

# Q1.2
class Sessions2:

    def __init__(self):
        self.current = []
        self._abonnement = False

    def add(self, session):
        if not self._abonnement and len(self.current) >= 1:
            raise LimiteNombreSessionAtteintError()
        self.current.append(session)

    def current_sessions(self):
        return self.current

    def kill(self):
        for session in self.current:
            session.kill()

    def abonnement(self):
        self._abonnement = True

class LimiteNombreSessionAtteintError(Exception):
    pass

# Q1.3
class Sessions:

    def __init__(self, session_policy):
        self.current = []
        self.session_policy = session_policy

    def add(self, session):
        if self.session_policy.capacity_reached(len(self.current)):
            raise LimiteNombreSessionAtteintError()
        else:
            self.current.append(session)

    def current_sessions(self):
        return self.current

    def kill(self):
        for session in self.current:
            session.kill()

    def abonnement(self):
        self._abonnement = True
