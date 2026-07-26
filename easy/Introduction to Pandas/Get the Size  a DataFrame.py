import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0],players.shape[1]] # players.shape - возвращает кортеж, [0] [1] - строки и столбцы
