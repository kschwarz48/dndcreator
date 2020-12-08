import random
# Group Members: Kevin, Josiah, Paul
# Description: D&D algorithm

class Character:

    def __init__(self):
        self.race = "" 
        self.player_name = ""
        self.character_name = ""
        self.height = 0 
        self.weight = 0
        self.hair_color = ""
        self.eye_color = ""
        self.player_class = ""    
        self.health_points = 0
        self.equipment = [""]
        self.armor_class = 0
        self.Attributes = {
        "Strength": 0, "Dexterity": 0, "Constitution": 0,
        "Wisdom": 0, "Charisma": 0, "Intelligence": 0
        }
        self.cantrips = {"No Cantrips"}
        self.spells = {"No Spells"}
        self.stat_rolls = list(random.sample(range(3, 18), 6))

    def roll_stats(self):
        """
        Rolls and assigns player stats
        """
        print("---STAT ASSIGNMENT---")
        print("Rolling for stats...\nYour stats are: ",  self.stat_rolls)
        
        for key in self.Attributes:
            if self.Attributes[key] != 0:
                continue
            self.Attributes[key] = int(input("Assign a number for " + str(key) + ": "))
            if self.Attributes[key] not in self.stat_rolls:
                print("Invalid Entry")
                self.Attributes[key] = 0
                self.roll_stats()
                break
            print(self.Attributes[key], "has been assigned to ", key, "\n")
            self.stat_rolls.remove(int(self.Attributes[key]))
            if len(self.stat_rolls) > 0:
                print("Your stats are: ",  self.stat_rolls)
            else:
                print("Your stats have been assigned as follows: ", self.Attributes)
                self.set_equipment()
        
    def set_character_name(self):
        """
        Sets character name based on input
        """
        self.character_name = input("\nPlease enter the character's name: ")
        self.set_player_name()
        
    def set_player_name(self):
        """
        Sets player name based on input
        """
        self.player_name = input("\nPlease enter the player's name: ")
        self.set_race()

    def set_height_weight(self):
        """
        Sets height (in inches) and weight based on race and dice rolls
        """
        if self.race == "human":
            height = 56 + random.randint(2,20)
            weight = 110 * random.randint(2,8)
            
        elif self.race == "dwarf":
            height = 44 + random.randint(2,8)
            weight = 115 * random.randint(2,12)
            
        elif self.race == "elf":
            height = 54 + random.randint(2,20)
            weight = 90 * random.randint(1,4)
            
        elif self.race == "halfling":
            height = 31 + random.randint(2,8)
            weight = 35
        
        self.height = height
        self.weight = weight
        print("\nRolling for height...")
        print("Your character's height is " + str(height // 12) + " feet " + str(height % 12) + " inches.")
        print("\nRolling for weight...")
        print("Your character's weight is " + str(weight) + " pounds.")
        self.set_hair_color()
        
    def set_hair_color(self):
        """
        Sets hair and eye color based on input
        """
        self.hair_color = input("\nPlease enter your character's hair color: ")
        self.set_eye_color()
        
    def set_eye_color(self):
        """
        Sets eye color based on input
        """
        self.eye_color = input("\nPlease enter your character's eye color: ")
        self.set_class()

    def roll_health_points(self):
        """
        Returns player health points
        """
        health_points = 0
        bonus_health = 3
        if self.player_class == "Fighter":
            health_points = (10 + bonus_health)
        elif self.player_class == "Cleric":
            health_points = (8 + bonus_health)
        elif self.player_class == "Wizard":
            health_points = (6 + bonus_health)     
        elif self.player_class == "Bard":
            health_points = (8 + bonus_health)    
        elif self.player_class == "Rogue":
            health_points = (8 + bonus_health)   
               
        return health_points

    def set_class(self):
        """
        Receives input for character class
        Sets player class
        """
        print("\nSelect a class from the following list for your character:\n")
        print("---Fighter---\n" +

        "DESCRIPTION: Every fighter can pick up a weapon and wield it ably. Likewise, a fighter is adept with shields and every form of armor. "+

        "Beyond that basic degree of familiarity, each fighter specializes in a certain style of combat. Some concentrate on archery, some on fighting with two weapons at once, and some augmenting their martial skills with magic."+

        "This combination of broad general ability and extensive specialization makes fighters superior combatants.\n\n---Rogue---\n" +

        "DESCRIPTION: Rogues rely on skill, stealth, and thier foes' vunerability to get the upper hand in any situation.\n"+

        "They have a knack for finding the solution to just about problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful advernturing party.\n\n---Bard---\n" +

        "DESCRIPTION: Whether poet, scholar, or scoundrel, a bard eaves magic through words and music to inspire allies, demoralize\n"+
        "foes, manipulated minds, and heal wounds. The bard is a master of song, speech, and the magic they contain.\n\n---Cleric---\n" +

        "DESCRIPTION: Clerics are intermediaries between the mortal world and the distant planes of the gods.\n"+

        "As varied as the gods they serve, clerics strive to embody the handiwork of their dieties and are imbued with magic.\n\n---Wizard---\n" +

        "DESCRIPTION: Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning,\n"+

        "subtle deception, and brute-force mind control.\n")
        class_input = input("Choose your class: ")
        
        if class_input.lower() == "fighter":
            self.player_class = "Fighter"
            print("\nFighter is a great choice! Get ready to defend your name!\n")
            self.roll_stats()
            print("Rolling health points...  health points rolled.")
            #cantrip/spell method call(0,0)
            #we can change this method call
            
        elif class_input.lower() == "wizard":
            self.player_class = "Wizard"
            print("\nWizard is a great choice! Lets see those wizard skills at work!\n")
            self.roll_stats()
            print("Rolling health points...  health points rolled.")
            #cantrip/spell method call(3,2)
            
        elif class_input.lower() == "cleric":
            self.player_class = "Cleric"
            print("\nCleric is a great choice, but how clerical can you be?\n")
            self.roll_stats()
            print("Rolling health points...  health points rolled.")
            #cantrip/spell method call(3,2)
            
        elif class_input.lower() == "bard":
            self.player_class = "Bard"
            print("\nBard is a great choice! Show eveyrone who's best!\n")
            self.roll_stats()
            print("Rolling health points...  health points rolled.")
            #cantrip/spell method call(2,2)
            
        elif class_input.lower() == "rogue":
            self.player_class = "Rogue"
            print("\nRogue is a great choice! Lets see those rogue skills at work!\n")
            self.roll_stats()
            print("Rolling health points...  health points rolled.")
            #cantrip/spell method call(0,0)
            
        else:
            print("Invalid")
            self.set_class()
            
    def set_abilities(self):
        """
        Sets player abilities
        """
        
        print("\nSelect abilities for your character:\n")
        

        if self.player_class == "Wizard":
            print("     Cantrips (pick 3)\nMage Hand\nMage Armor\nRay of Frost\nFire Bolt\nLight\n")      
            

            cantrip_1 = input("Enter your first cantrip selection: ")
            cantrip_2 = input("Enter your second cantrip selection: ")
            cantrip_3 = input("Enter your third cantrip selection: ")

            print("     Level 1 Spells (pick 2)\nBurning Hands\nCharm Person\nDetect Magic\nFeather Fall\nFireball")
            
            spell_1 = input("Enter your first spell: ")
            spell_2 = input("Enter your second spell: ")
            
            cantrips = {
            "Cantrip 1": cantrip_1, "Cantrip 2": cantrip_2, "Cantrip 3": cantrip_3
            }
                
            spells = {
            "Spell 1": spell_1,"Spell 2": spell_2
            }



        elif self.player_class == "Cleric":
            print("     Cantrips (pick 3)\nMage Hand\nMending\nAcid Splash\nGuidance\nLighor\nGuiding Bolt\nHealing Word\n")
                 
            cantrip_1 = input("Enter your first cantrip selection: ")
            cantrip_2 = input("Enter your second cantrip selection: ")
            cantrip_3 = input("Enter your third cantrip selection: ")

            print("     Level 1 Spells (pick 2)\nBless\nCure Wounds\nDivine Favor\nGuiding Bolt\nHealing Word")
            spell_1 = input("Enter your first spell: ")
            spell_2 = input("Enter your second spell: ")

            cantrips = {
            "Cantrip 1": cantrip_1, "Cantrip 2": cantrip_2, "Cantrip 3": cantrip_3
            }
                
            spells = {
            "Spell 1": spell_1,"Spell 2": spell_2
            }
            
        elif self.player_class == "Bard":
            print("     Cantrips (pick 2)\nMage Hand\nMinor Illusion\nPrestidigitation\nThaumaturgy\nVicious Mockery\n")
            
            cantrip_1 = input("Enter your first cantrip selection: ")
            cantrip_2 = input("Enter your second cantrip selection: ")

            print("     Level 1 Spells (pick 2)\nThunder Wave\nSleep\nSilent Image\nShield\nIdentify")	
            
            spell_1 = input("Enter your first spell: ")
            spell_2 = input("Enter your second spell: ")      

            cantrips = {
            "Cantrip 1": cantrip_1, "Cantrip 2": cantrip_2
            }
                
            spells = {
            "Spell 1": spell_1,"Spell 2": spell_2
            }
        
        else:
            print("This Player Class does not aquire any abilities\n")
            spells = {""}
            cantrips = {""}
            
        self.cantrips = cantrips
        self.spells = spells
 
            
    def set_equipment(self):
        """
        Sets player equipment
        """

        print("\nSelect equipment for your character:")
        one_hand_full = False
        self.armor_class = 0

        if self.player_class == "Fighter":
            shield_choice = input("Would you like to use a shield? (Armor Class +2, but 2-handed weapons will not be available)? y/n: ")
            if shield_choice.lower() == "y":
                self.armor_class += 2
                self.equipment.append("Shield (AC+2)")
                one_hand_full = True
            elif shield_choice.lower() == "n":
                one_hand_full = False
            else:
                self.set_equipment()
            print("\nSelect your armor from the following list:")
            print("Plate        (Armor Class 18, Sneak Disadvantage)")
            print("Half-Plate   (Armor Class 15)")
            armor_choice = input()
            if armor_choice.lower() == "plate":
                self.armor_class += 18
                self.equipment.append("Plate (AC 18, Sneak Disadvantage)")
            elif armor_choice.lower() == "half-plate":
                self.armor_class += 15
                self.equipment.append("Half-Plate (AC 15)")
            else:
                print("\nInvalid choice. Please choose equipment again.\n")
                self.equipment = []
                self.set_equipment()
            print("\nNow select your weapon. ")
            if one_hand_full == False:
                print("Battleaxe        (2-handed, 1d8)")
                print("Heavy Crossbow   (2-handed, 1d10, range 150/600)")
            print("Shortsword       (1-handed, 1d6)")
            weapon_choice = input()
            if one_hand_full == False:
                if weapon_choice.lower() == "battleaxe":
                    self.equipment.append("Battleaxe (2-handed, 1d8)")
                elif weapon_choice.lower() == "heavy crossbow":
                    self.equipment.append("Heavy Crossbow (2-handed, 1d10, range 150/600)")
            if weapon_choice.lower() == "shortsword":
                self.equipment.append("Shortsword (1-handed, 1d6)")
            else:
                print("\nInvalid choice. Please select equipment again.\n")
                self.equipment = []
                self.set_equipment()


        elif self.player_class == "Wizard":
            print("\nPlease select your weapon from the following list:")
            print("Dagger       (1d4)")
            print("Quarterstaff (1d6)")
            weapon_choice = input()
            if weapon_choice.lower() == "dagger":
                self.equipment.append("Dagger (1d4)")
                self.set_abilities()
            elif weapon_choice.lower() == "quarterstaff":
                self.equipment.append("Quarterstaff (1d6)")
                self.set_abilities()
            else:
                print("\nInvalid choice. Please select equipment again.\n")
                self.equipment = []
                self.set_equipment()
                
                
        elif self.player_class == "Cleric":
            shield_choice = input("Would you like to use a shield? (Armor Class +2)? y/n")
            if shield_choice.lower() == "y":
                self.armor_class += 2
                self.equipment.append("Shield (AC+2)")
            print("\nSelect your armor from the following list:")
            print("Scale-mail    (Armor Class 14)")
            print("Breastplate   (Armor Class 14)")
            armor_choice = input()
            if armor_choice.lower() == "scale-mail":
                self.armor_class += 14
                self.equipment.append("Scale-mail (AC 14)")
                self.set_abilities()
            elif armor_choice.lower() == "breastplate":
                self.armor_class += 14
                self.equipment.append("Breastplate (AC 14)")
                self.set_abilities()
            else:
                print("\nInvalid choice. Please choose equipment again.\n")
                self.equipment = []
                self.set_equipment()
            print("\nNow select your weapon. ")
            print("Mace         (1-handed, 1d6)")
            print("Flail        (1-handed, 1d8")
            weapon_choice = input()
            if one_hand_full == False:
                if weapon_choice.lower() == "mace":
                    self.equipment.append("Mace (1-handed, 1d6)")
                    self.set_abilities()
                elif weapon_choice.lower() == "flail":
                    self.equipment.append("Flail (1-handed, 1d8)")
                    self.set_abilities()
            else:
                print("\nInvalid choice. Please select equipment again.\n")
                self.equipment = []
                self.set_equipment()
        
        
        elif self.player_class == "Bard":
            print("The bard uses Leather Armor (Armor Class 11).")
            self.armor_class += 11
            self.equipment.append("Leather Armor (AC 11)")
            print("\nNow select your weapon. ")
            print("Club         (1-handed, 1d4)")
            print("Spear        (1-handed, 1d6")
            weapon_choice = input()
            if weapon_choice.lower() == "club":
                self.equipment.append("Club (1-handed, 1d4)")
                self.set_abilities()
            elif weapon_choice.lower() == "spear":
                self.equipment.append("Spear (1-handed, 1d6)")
                self.set_abilities()
            else:
                print("\nInvalid choice. Please select equipment again.\n")
                self.equipment = []
                self.set_equipment()
            

        elif self.player_class == "Rogue":
            print("\nSelect your armor from the following list:")
            print("Leather Armor    (Armor Class 11)")
            print("Studded Leather   (Armor Class 13)")
            armor_choice = input()
            if armor_choice.lower() == "leather armor":
                self.armor_class += 11
                self.equipment.append("Leather Armor (AC 11)")
            elif armor_choice.lower() == "studded leather":
                self.armor_class += 13
                self.equipment.append("Studded Leather (AC 13)")
            else:
                print("\nInvalid choice. Please choose equipment again.\n")
                self.equipment = []
                self.set_equipment()
            print("\nNow select your weapon. ")
            print("Dual-Wield Short Swords   (2d6)")
            print("Light Crossbow            (1d8, range 80/320)")
            weapon_choice = input()
            if weapon_choice.lower() == "dual-wield short swords":
                self.equipment.append("Dual-Wield Short Swords (2d6)")
            elif weapon_choice.lower() == "light crossbow":
                self.equipment.append("Light Crossbow (1d8, range 80/320)")
            else:
                print("\nInvalid choice. Please select equipment again.\n")
                self.equipment = []
                self.set_equipment()
           
    
    def get_race(self):
        """
        Returns player race
        """
        return self.race

    def set_race(self):
        """
        Receives input for character race
        Sets player race
        """
        print("\nSelect a race from the following list for your character:\nDwarf\nElf\nHalfling\nHuman\n")
        race_input = input("Choose your race: ")
        self.race = race_input.lower()
        if self.race == "dwarf" or self.race == "elf" or self.race == "halfling" or self.race == "human":
            self.set_height_weight()
        else:
            print("\nInvalid\n")
            self.set_race()
        
    def print_character_description(self):
        """
        Print character description.
        """
        print("==========Character Description==========")
        print("Player Name:     " + self.player_name.capitalize())
        print("Character Name:  " + self.character_name.capitalize())
        print("Race:            " + self.race.capitalize())
        print("Class:           " + self.player_class)
        print("Height:          " + str(self.height//12) +" feet " + str(self.height%12) + " inches")
        print("Weight:          " + str(self.weight) + " lbs")
        print("Eye Color:       " + self.eye_color.capitalize())
        print("Hair Color:      " + self.hair_color.capitalize())
        print("HP:              " + str(self.roll_health_points()))
        print("\n=============Attribute List=============")
        print("ATTRIBUTES:\n")
        for key in self.Attributes:
            print(key + ": " + str(self.Attributes[key]))
        if self.player_class == "Fighter" or self.player_class == "Rogue":
            print("")
        else:   
            print("\n===============Abilities================")
            print("SPELLS:\n")
            for key in self.spells:
                print(key + ": " + str(self.spells[key].capitalize()))
            print("\nCANTRIPS:\n")
            for key in self.cantrips:
                print(key + ": " + str(self.cantrips[key].capitalize()))
        print("\n===============Equipment================")
        print("EQUIPMENT:")
        for item in self.equipment:
            print(item)
        print("Armor Class: " + str(self.armor_class) + "\n")
        print("========================================")  


def main():
    """
    Main method
    """
    Character1 = Character()
    
    print("Welcome to the D&D Character Creator!")
    print("This program will guide you through the character creation process to create a ready-to-play character.")
    
    Character1.set_character_name()  #FIRST METHOD CALL
    Character1.print_character_description()
            
    Character1.print_character_description()   
    print("Goodbye!")
    
    
if __name__ == "__main__":
    main()