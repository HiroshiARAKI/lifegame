# LifeGame on Python

![version](https://img.shields.io/badge/version-0.1.0-lightgray.svg?style=flat) 
   
You can simulate Conway's Game of Life simply on Python!!  

## What is Conway's Game of Life?
  
(en) [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)  
(jp) [ライフゲーム - Wikipedia](https://ja.wikipedia.org/wiki/ライフゲーム)  


## Examples
The code of [main.py](main.py)
```python
from lifegame import GUILifeGame


if __name__ == '__main__':

    # Create Conway's Game of Life GUI Frame
    game = GUILifeGame(f_shape=(50, 50), time_step=100)

    # Start!!
    game.run(init_rand=True, rate=0.2)
```
![example-1](examples/img1.png)

## LICENSE
[MIT LICENSE](LICENSE.txt)  
Copyright (c) 2019 Hiroshi ARAKI