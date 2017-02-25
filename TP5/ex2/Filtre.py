
class Filtre():
    def filtrer_par_priorite_inf(self, priorite, log):
        if(log.get_priority() >= priorite):
            return log
        return None
