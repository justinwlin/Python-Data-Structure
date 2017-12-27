def main():
    str = [1,2,3]
    str2 = str
    str.append(1)

    print(str)
    print(str2)

main()

if bolt.is_player_bolt():
    x = bolt.x
    y = bolt.y
    return (self.contains((x - BOLT_WIDTH / 2, y + BOLT_HEIGHT / 2)) or @ CHECK
            self.contains((x - BOLT_WIDTH / 2, y - BOLT_HEIGHT / 2)) or @
            self.contains((x + BOLT_WIDTH / 2, y - BOLT_HEIGHT / 2)) or
            self.contains((x + BOLT_WIDTH / 2, y + BOLT_HEIGHT / 2))) #CHECK

if bolt.is_player_bolt():
            return (self.contains((bolt.leftx, bolt.upy)) @ - +
            or self.contains((bolt.rightx, bolt.upy)) @ + +
            or self.contains((bolt.leftx, bolt.downy))@ - -
            or self.contains((bolt.rightx, bolt.downy)))@ + -


        self.leftx = self.x - BOLT_WIDTH / 2
        self.rightx = self.x + BOLT_WIDTH / 2
        self.downy = self.y - BOLT_HEIGHT / 2
        self.upy = self.y + BOLT_HEIGHT / 2

