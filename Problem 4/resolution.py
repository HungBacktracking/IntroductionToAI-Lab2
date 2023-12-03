class LOGIC_RESOLUTION:
    def __init__(self, _alpha, _KB):
        inverse_alpha = []
        for val in self.preprocess(_alpha):
            inverse_alpha.append(self.inverse(val))
        
        for clause in _KB:
            self.KB.append(self.preprocess(clause))

        for val in inverse_alpha:
            if [val] not in self.KB:
                self.KB.append([val])

    @staticmethod
    def preprocess(clause):
        literal_list = []
        for val in clause.split(' '):
            if len(val) > 0 and val != "OR":
                literal_list.append(val)
        
        return literal_list
    
    @staticmethod
    def inverse(literal):
        if '-' in literal:
            return literal.replace('-', '')
        return '-' + literal
    
    @staticmethod
    def is_inverse(literal_a, literal_b):
        return LOGIC_RESOLUTION.inverse(literal_a) == literal_b
    
    @staticmethod
    def is_valid(clause):
        for i in range(len(clause) - 1):
            for j in range(len(clause)):
                if LOGIC_RESOLUTION.is_inverse(clause[i], clause[j]):
                    return True
                
        return False
    
    @staticmethod
    def is_sublist_of(l1, l2):
        for element in l1:
            if not element in l2:
                return False
        return True
    
    @staticmethod
    def pl_resolve(clause_a, clause_b):
        resolvents = []
        for i in range(len(clause_a)):
            for j in range(len(clause_b)):
                    if LOGIC_RESOLUTION.is_inverse(clause_a[i], clause_b[j]):
                        resolvent = clause_a[:i] + clause_a[i + 1:] + clause_b[:j] + clause_b[j + 1:]
                        resolvents.append(resolvent)

        return resolvents
    
    def PL_RESOLUTION(self):
        new = []
        clauses = self.KB

        isTrue = False
        while True:
            for i in range(len(self.KB) - 1):
                for j in range(len(self.KB)):
                    resolvents = self.pl_resolve(self.KB[i], self.KB[j])

                
                if [] in resolvents:
                    isTrue = True

    

