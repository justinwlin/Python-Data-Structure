def __str__(self):
    def iter_string(nlist, height):
        MAX_STR = 2
        if height < 0:
            return ''
        # l -= len(dta)//2
        newlist = []
        s = ''
        first_elem = True
        for n in nlist:
            dta = ' ' + '-' * (MAX_STR) + ' '
            if n is None:
                newlist += [None, None]
            else:
                dtas = str(n.data)
                if len(dtas) < MAX_STR:
                    dtas += (MAX_STR - len(dtas)) * ' '
                elif len(dtas) > MAX_STR:
                    dtas = dtas[:MAX_STR]
                dta = '[' + dtas + ']'
                newlist.append(n.left)
                newlist.append(n.right)
            l = 2 ** (height + len(dta) // 2 - 1) - len(dta) // 2
            s += ' ' * l + str(dta) + ' ' * l
        s += '\n'
        s += iter_string(newlist, height - 1)

        return s

    return iter_string([self.root], self.height())