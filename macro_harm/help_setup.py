def srandy():
    print('Help spell:')
    helpSpell = input()

    print("harm spell")
    harmSpell = input()


    print ("#showtooltip")
    print("/cast [help] " +helpSpell + "; [harm] Insect Swarm")



def helpHarmMacro(helpSpell, harmSpell):
    print("#showtooltip")
    print("/cast [help] " +helpSpell + "; [harm] " +harmSpell)
    print("/cast [help,nodead][@player] "+helpSpell)


helpHarmMacro("Nourish", "Faerie Fire")