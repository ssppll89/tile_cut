from PIL import Image

img = Image.open("test.png")

tile_w = int(input("Tile width:"))
tile_h = int(input("Tile height:"))
tile_m = int(input("Tile margin:"))
tile_s = int(input("Tile separaton:"))

num_tiles = (img.width // tile_w)

new_img = Image.new("RGBA", ( (img.width // tile_w) * ((tile_s*2)+tile_w)  , (img.height // tile_h) * ((tile_s*2)+tile_h)), (1,1,1,0))

for a in range((num_tiles * num_tiles)):
	x = ((img.width // 2) - ((tile_w // 2) * (a//4)) - (tile_w // 2)) + ((tile_w // 2) * (a%num_tiles))
	y = ((tile_h // 2) * (a % num_tiles))+ ((tile_h // 2) * ( a // num_tiles ))
	cropped = img.crop((x, y, x+tile_w, y+tile_h))
	new_img.paste(cropped, ( (a % num_tiles ) * tile_w, ( a // num_tiles ) * tile_h ), Image.open("mask.png"))

new_img.save("tiles_save.png")
