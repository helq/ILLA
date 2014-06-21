from functools import reduce
def λ_term_to_str(λ_term):
    if λ_term['type'] == 'value':
        if type(λ_term['value']) is tuple:
            v1 = λ_term_to_str( {'type': 'value', 'value': λ_term['value'][0]} )
            v2 = λ_term_to_str( {'type': 'value', 'value': λ_term['value'][1]} )
            return "("+ str(v1) +":"+ str(v2) +")"
        if type(λ_term['value']) is bool:
            return "true" if λ_term['value'] else "false"
        if λ_term['value'] == "nil":
            return "nil"
        return repr(λ_term['value'])

    if λ_term['type'] == 'id': return λ_term['id']

    if λ_term['type'] == 'op':
        return ( "("
               + λ_term_to_str(λ_term['val1'])
               + λ_term['op']
               + λ_term_to_str(λ_term['val2'])
               + ")")

    if λ_term['type'] == 'λ_abstraction':
        return ( "λ"
               + λ_term['param']
               + ".("
               + λ_term_to_str(λ_term['λ_term'])
               + ")")

    if λ_term['type'] == 'λ_application':
        return ("(" + λ_term_to_str(λ_term['function'])+") "
                + reduce( lambda x,y: x+y,
                          map(lambda x: "("+λ_term_to_str(x)+")", λ_term['input'])
                        )
               )

