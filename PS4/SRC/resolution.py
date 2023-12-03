class LOGIC_RESOLUTION:
    def __init__(self, _alpha, _KB):
        self.KB = []
        self.isTrue = False
        self.output_clauses = []

        inverse_alpha = []
        for val in self.preprocess(_alpha):
            inverse_alpha.append(self.inverse(val))
        
        for clause in _KB:
            self.KB.append(self.preprocess(clause))

        for val in inverse_alpha:
            if [val] not in self.KB:
                self.KB.append(self.standardize([val]))

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
    def is_always_valid(clause):
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
    def standardize(clause):
        # Removing duplicates from clause.
        unique = set(clause)

        return sorted(list(unique), key = lambda x: x[-1])

    @staticmethod
    def pl_resolve(clause_a, clause_b):
        resolvents = []
        for i in range(len(clause_a)):
            for j in range(len(clause_b)):
                    if LOGIC_RESOLUTION.is_inverse(clause_a[i], clause_b[j]):
                        resolvent = clause_a[:i] + clause_a[i + 1:] + clause_b[:j] + clause_b[j + 1:]
                        resolvents.append(LOGIC_RESOLUTION.standardize(resolvent))

        return resolvents
    
    def PL_RESOLUTION(self):
        newList = []
        clauses = self.KB
        while True:
            self.output_clauses.append([])
            for i in range(len(clauses)):
                for j in range(len(clauses)):
                    resolvents = self.pl_resolve(clauses[i], clauses[j])

                    if [] in resolvents:
                        self.isTrue = True
                    for temp in resolvents:
                        if self.is_always_valid(temp):
                            continue
                        if not temp in newList and not temp in clauses and not temp in self.output_clauses[-1]:
                            newList.append(temp)
                            self.output_clauses[-1].append(temp)

            if self.is_sublist_of(newList, clauses):
                return False
            for temp in newList:
                if not temp in clauses:
                    clauses.append(temp)
            if self.isTrue == True:
                return True
            
    @staticmethod
    def cnf_format(clause):
        result = ''
        if len(clause) == 0:
            return '{}'
        elif len(clause) == 1:
            return clause[0]
        else:
            for literal in clause[:-1]:
                result += literal
                result += ' OR '
            result += clause[-1]
        
        return result
            
    def output(self, file):
        for i in range(len(self.output_clauses)):
            print(len(self.output_clauses[i]), file = file)
            for j in range(len(self.output_clauses[i])):
                print(self.cnf_format(self.output_clauses[i][j]), file = file)
        
        print('YES' if self.isTrue else 'NO', file = file)


    

