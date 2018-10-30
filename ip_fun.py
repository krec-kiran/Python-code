def numberAndIPaddress(ip):
    if '.' in ip:
        ip = ip.split('.')
        val = ''
        for i in ip:
            val += str(format(int(i), '08b'))
        k = int(val, 2)
        return(str(k))
    else:
        binary = str((format(int(ip), '08b')))
        if len(binary) < 32:
            binary = '0' * (32 - len(binary)) + str(binary)
        ip_address = ''
        start = 0
        end = 8
        while end <= len(binary):
            ip_address += str(int(str(binary[start:end]), 2)) + '.'
            start += 8
            end += 8
        return(ip_address.strip('.'))
