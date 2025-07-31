import itertools
from typing import List, Dict, Set

class LeetTransliterator:
    def __init__(self):
        self.LEET_MAP = {
            'а': ['4', 'a', 'A', '@' , '/-\\'],
            'б': ['6', 'b', 'B'],
            'в': ['v', 'V', 'b', '8'],
            'г': ['r', 'R', 'g' '|¯'],
            'д': ['d', 'D', 'g', 'q'],
            'е': ['e', 'E', '3' ],
            'ё': ['e', 'E', '3'],
            'ж': ['x', 'X', '>|<' , '><' , '*' '}|{' , ']|[' ],
            'з': ['3', 'z', 'Z'],
            'и': ['u', 'U', 'i', 'I' 'N'],
            'й': ['u', 'U', 'i', 'I' 'ū' , 'Ū'],
            'к': ['k', 'K', 'c' , '/<' , '|<'],
            'л': ['l', 'L', '1', 'JI' , 'J1' , 'jl' ],
            'м': ['m', 'M', '/\\/\\', '|\\/|', '1\\/1'],
            'н': ['n', 'N', 'H', '|-|' , 'h' , '1-1' , 'l-l'],
            'о': ['0', 'o', 'O'],
            'п': ['p', 'P', 'n' , 'II' , 'll' , '|¯|' , '/¯/' , '/7'],
            'р': ['p', 'P', 'r', 'R'],
            'с': ['c', 'C', 's', 'S', '5' '₡' , '('],
            'т': ['t', 'T', '7' , '7¯'],
            'у': ['y', 'Y', 'u', 'U'],
            'ф': ['f', 'F', 'ph' , 'qp' , 'c|ɔ' ],
            'х': ['x', 'X' , '}{' , ']['],
            'ц': ['c', 'C', 'u,' , '|_|,'],
            'ч': ['4', 'ch'],
            'ш': ['w', 'W', 'sh' , 'uu' , 'LLI' , 'LL1' , 'LII' , 'L11' , 'L||' , '|//' , 'l11'],
            'щ': ['w', 'W', 'sh' , 'w,' , 'uu,' ,'LII,', 'L||,' , 'LLI,' , 'l11,' , '|//,'],
            'ъ': ['`b' , '¯b' , '-b' ],
            'ы': ['bl', '6I' , '6i' , 'b1' , 'bI'],
            'ь': ['b'],
            'э': ['e', 'E', '3'],
            'ю': ['10', 'y0', 'yu' , '1-0' , 'I-0' , 'i-o' , '1-o' , 'l-O' , '|-O' , '|-o' '|O'],
            'я': ['9', 'ya', 'R' , '9I' , '9\\'],
            'a': ['4', 'a', 'A', '@'],
            'b': ['6', 'b', 'B' , '|b' , ''],
            'c': ['c', 'C', '(' , '₡'],
            'd': ['d', 'D' , 'o|' , '|)'],
            'e': ['3', 'e', 'E' ],
            'f': ['f', 'F' ],
            'g': ['9', 'g', 'G', '6'],
            'h': ['h', 'H' , '|n'],
            'i': ['1', 'i', 'I', '!'],
            'j': ['j', 'J'],
            'k': ['k', 'K' , '/<' , '|<'],
            'l': ['1', 'l', 'L', '|' , 'I'],
            'm': ['m', 'M', '/\\/\\', '|\\/|', '1\\/1'],
            'n': ['n', 'N' , 'И'],
            'o': ['0', 'o', 'O'],
            'p': ['p', 'P'],
            'q': ['q', 'Q'],
            'r': ['r', 'R'],
            's': ['5', 's', 'S', '$'],
            't': ['7', 't', 'T', '+' , '7¯'],
            'u': ['u', 'U' ],
            'v': ['v', 'V' ],
            'w': ['w', 'W' , '\\/\\/'] ,
            'x': ['x', 'X' , '}{' , ']['],
            'y': ['y', 'Y'],
            'z': ['2', 'z', 'Z'],
            
            '0': ['0'], '1': ['1'], '2': ['2'], '3': ['3'], '4': ['4'],
            '5': ['5'], '6': ['6'], '7': ['7'], '8': ['8'], '9': ['9'],
            ' ': [' ', '_', '-'], 
            '-': ['-', '_'], 
            '_': ['_', '-'],
            '.': ['.'],
            '!': ['!'],
            '?': ['?'],
            '@': ['@'],
            '#': ['#'],
            '$': ['$'],
            '%': ['%'],
            '&': ['&'],
            '*': ['*'],
            '(': ['('],
            ')': [')'],
            '+': ['+'],
            '=': ['='],
            '[': ['['],
            ']': [']'],
            '{': ['{'],
            '}': ['}'],
            '|': ['|'],
            '\\': ['\\'],
            '/': ['/'],
            ':': [':'],
            ';': [';'],
            '"': ['"'],
            "'": ["'"],
            '<': ['<'],
            '>': ['>'],
            ',': [',']
        }
        
        self.POPULAR_TERMS = {
            'vip': ['VIP', 'v1p', 'V1P', 'vLp', 'V|P'],
            'dead': ['dead', 'de4d', 'D34d', 'DEAD', 'D34D'],
            'inside': ['inside', '1nside', 'ins1de', '1ns1de', 'iNs1De', '1N51D3'],
            'killer': ['killer', 'k1ller', 'ki11er', 'k1ll3r', 'K1LL3R', 'KILLER'],
            'player': ['player', 'pl4yer', 'play3r', 'pl4y3r', 'P14Y3R', 'PLAYER'],
            'gamer': ['gamer', 'g4mer', 'gam3r', 'g4m3r', 'G4M3R', 'GAMER'],
            'pro': ['pro', 'pr0', 'PR0', 'Pro'],
            'noob': ['noob', 'n00b', 'N00B', 'n0ob' , 'n006' ],
            'lol': ['lol', '101', 'LOL', 'L0L'],
            'ez': ['ez', 'EZ', '32'],
            'gg': ['gg', 'GG', '99'],
            'wp': ['wp', 'WP'],
            'god': ['god', 'g0d', 'G0D', 'GOD'],
            'king': ['king', 'k1ng', 'K1NG', 'KING'],
            'boss': ['boss', 'b0ss', 'B0SS', 'BOSS' , 'B0$$']
        }
    
    def generate_all_variants(self, text: str) -> List[str]:
        """Generate all possible leet speak variants of the input text"""
        text = text.lower()
        variants = set()
        
        lower_text = text.lower()
        for term, term_variants in self.POPULAR_TERMS.items():
            if term in lower_text:
                for variant in term_variants:
                    modified_text = lower_text.replace(term, variant)
                    variants.update(self._generate_character_variants(modified_text))
        
        variants.update(self._generate_character_variants(text))
        
        unique_variants = list(variants)
        unique_variants.sort()
        
        if len(unique_variants) > 200:
            unique_variants = unique_variants[:100] + unique_variants[-100:]
            unique_variants = list(set(unique_variants)) 
            unique_variants.sort()
        
        return unique_variants
    
    def _generate_character_variants(self, text: str) -> Set[str]:
        """Generate variants by replacing characters with leet speak equivalents"""
        variants = set()
        
        char_options = []
        for char in text:
            if char in self.LEET_MAP:
                char_options.append(self.LEET_MAP[char])
            else:
                char_options.append([char])
        
        total_combinations = 1
        for options in char_options:
            total_combinations *= len(options)
        
        if total_combinations > 1000:
            variants.update(self._sample_variants(char_options, 500))
        else:
            for combination in itertools.product(*char_options):
                variant = ''.join(combination)
                variants.add(variant)
        
        return variants
    
    def _sample_variants(self, char_options: List[List[str]], max_samples: int) -> Set[str]:
        """Sample variants when there are too many combinations"""
        import random
        variants = set()
        
        original = ''.join(options[0] for options in char_options)
        variants.add(original)
        
        for _ in range(max_samples - 1):
            combination = []
            for options in char_options:
                combination.append(random.choice(options))
            variant = ''.join(combination)
            variants.add(variant)
        
        for i in range(min(20, len(char_options))):
            combination = []
            for j, options in enumerate(char_options):
                if j == i and len(options) > 1:
                    combination.append(options[1]) 
                else:
                    combination.append(options[0])
            variant = ''.join(combination)
            variants.add(variant)
        
        combination = []
        vowels = set('аеёиоуыэюяaeiou')
        for char in char_options:
            if char[0].lower() in vowels and len(char) > 1:
                combination.append(char[1]) 
            else:
                combination.append(char[0]) 
        if combination:
            variant = ''.join(combination)
            variants.add(variant)
        
        return variants
    
    def get_character_variants(self, char: str) -> List[str]:
        """Get all possible variants for a single character"""
        return self.LEET_MAP.get(char.lower(), [char])
    
    def preview_mapping(self) -> str:
        """Return a string showing the character mapping for debugging"""
        result = "Character mapping preview:\n"
        for char, variants in sorted(self.LEET_MAP.items()):
            if char.isalpha(): 
                result += f"{char} -> {', '.join(variants)}\n"
        return result
