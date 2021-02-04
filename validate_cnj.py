def validate_cnj(cnj: str) -> bool:
    import re

    cnj = re.sub(r"[^0-9]", "", cnj).zfill(20)
    judicial_court = cnj[16:]
    digit = int(cnj[7:9])
    court = cnj[14:16]
    branch = cnj[13]
    initial_year = cnj[9:13]
    seq_number_size = len(cnj) - 13
    seq_number = cnj[0:seq_number_size]
    x = int(seq_number + initial_year + branch + court + judicial_court + '00')
    y = 97
    calculated_digit = 98 - x % y 
    
    return digit == calculated_digit
