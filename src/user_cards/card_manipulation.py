from PIL import Image, ImageDraw, ImageFont
import random
from decouple import config

FONT_PATH = config(
    "FONT_PATH",
    cast = str
)

FONT_NAME = config(
    "FONT_NAME",
    cast = str
)

USER_AVATARS_PATH = config(
    "USER_AVATARS_PATH",
    cast = str
)

class ImageManipulation:
    def __init__(self):
        self.width: float = 1920
        self.height: float = 512
        self.font_path: str = FONT_PATH
        self.font_name: str = FONT_NAME
        self.font_size: int = 50
        self.text: str = "No text at all"
        self.x_coord: int = 80
        self.y_coord: int = 80
        self.color_font: str = "#ffffff"
        self.color_background: str = "#000000"
        self.image_name: str = "output.png"

    def create_img(self,
                   width: int = 1920,
                   height: int = 512,
                   font_path: str = FONT_PATH,
                   font_name: str = FONT_NAME,
                   font_size: int = 50,
                   text: str = "No text at all",
                   x_coord: float = 80,
                   y_coord: float = 80,
                   color_font: str = "#ffffff",
                   color_background: str = "#000000",
                   image_name: str = "output.png"):
        
        self.width = width
        self.height = height
        self.font_path = font_path
        self.font_name = font_name
        self.font_size = font_size
        self.text = text
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color_font = color_font
        self.color_background = color_background
        self.image_name = image_name

        image = Image.new("RGB",
                          (self.width, self.height),
                          color=self.color_background)
        
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(f"{self.font_path}{self.font_name}",
                                  size=self.font_size)
        
        draw.text((self.x_coord, self.y_coord),
                  self.text,
                  fill=self.color_font,
                  font=font)
        
        image.save(self.image_name)

    def update_text(self,
                    new_text: str = "No text at all"):
        
        self.text = new_text

    def update_colors(self,
                      font_color: str = "#ffffff",
                      background_color: str = "#000000"):
        
        self.color_font = font_color
        self.color_background = background_color

    def update_dimensions(self,
                          width: int = 1920,
                          height: int = 512):
        
        self.width = width
        self.height = height

    def update_font(self,
                    font_path: str = FONT_PATH,
                    font_name: str = FONT_NAME,
                    font_size: int = 50):
        
        self.font_path = font_path
        self.font_name = font_name
        self.font_size = font_size

    def add_text(self,
                 text: str = "No text at all",
                 x_coord: float = 80,
                 y_coord: float = 80,
                 font_size: int = None,
                 font_color: str = None):
        
        font_size = font_size or self.font_size
        font_color = font_color or self.color_font

        image = Image.open(self.image_name)

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(f"{self.font_path}{self.font_name}",
                                  size=font_size)
        
        draw.text((x_coord, y_coord),
                  text,
                  fill=font_color,
                  font=font)
        
        image.save(self.image_name)

    def draw_circle_with_photo(self,
                               photo_name: str,
                               photo_path: str = USER_AVATARS_PATH,
                               x_coords: float = 80,
                               y_coords: float = 80,
                               diameter: int = 400,
                               border_width: int = 10,
                               smooth_edges: int = 20):

        image = Image.open(self.image_name)
        draw = ImageDraw.Draw(image)


        outer_left_up = (x_coords - diameter // 2 - border_width, y_coords - diameter // 2 - border_width)
        outer_right_down = (x_coords + diameter // 2 + border_width, y_coords + diameter // 2 + border_width)
        
        draw.ellipse([outer_left_up, outer_right_down], fill=None, outline="#FFFFFF", width=border_width)

        inner_left_up = (x_coords - diameter // 2, y_coords - diameter // 2)

        photo = Image.open(photo_path+photo_name).convert("RGBA")
        photo = photo.resize((diameter, diameter), Image.Resampling.LANCZOS)

        mask = Image.new("L", (diameter, diameter), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((smooth_edges, smooth_edges, diameter - smooth_edges, diameter - smooth_edges), fill=255)
        
        for i in range(smooth_edges):
            alpha = int(255 * (i / smooth_edges))
            mask_draw.ellipse(
                (i, i, diameter - i, diameter - i),
                outline=alpha,
                width=1
            )
        
        photo.putalpha(mask)

        image.paste(photo, inner_left_up, mask=photo)

        image.save(self.image_name)

class UserInfo:
    def __init__(self):
        self.user_name: str
        self.photo_name: str
        self.user_id: int
        self.user_status: str
        self.vpn_status: bool
        self.provider: str

    def card(self,
             user_name: str,
             photo_name: str,
             user_id: int,
             user_status: str,
             vpn_status: bool,
             provider: str):
        
        self.user_name = user_name
        self.photo_name = photo_name
        self.user_id = user_id
        self.user_status = user_status
        self.vpn_status = vpn_status
        self.provider = provider

        image = ImageManipulation()

        # Создание изображения
        image.create_img(text="Пользователь:",
                         x_coord=600,
                         y_coord=56,
                         font_name="Inter-Medium.ttf",
                         image_name=f"./user_cards/users_info_cards/{self.user_id}.png")

        # Добавление иконки
        image.draw_circle_with_photo(
            photo_name=self.photo_name,
            x_coords=300,
            y_coords=256,
            diameter=400,
            border_width=0,
            smooth_edges=3
        )

        # Добавление имени пользователя
        image.update_colors("#1283EB")

        image.add_text(text=self.user_name,
                       x_coord=980,
                       y_coord=56)
        image.update_colors("#ffffff")

        image.update_font("fonts/inter/", "Inter-Light.ttf", 45)

        image.add_text('ID:', 600, 120, 45)

        image.update_colors("#1283EB")
        image.add_text(self.user_id, x_coord=670, y_coord=120)
        image.update_colors("#ffffff")

        image.add_text('Статус:', 600, 175, 45)

        image.update_colors("#4BA0FC")
        image.add_text(self.user_status, 780, 175, 45)
        image.update_colors("#ffffff")

        image.add_text('Статус VPN:', 600, 230, 45)
        if self.vpn_status:
            image.update_colors("#84F40C")
            image.add_text("Active", 885, 230, 45)
        else:
            image.update_colors("#B60000")
            image.add_text("Deactive", 885, 230, 45)

        image.update_colors("#ffffff")

        image.update_colors("#ffffff")
        image.add_text('Количество потребляемого трафика: 12 ГБ', 600, 285, 45)

        image.add_text('Время использования VPN: Д:1 Ч:22 М:33', 600, 340, 45)


        image.add_text('Поставщик:', 600, 400, 45)
        image.update_colors("#F13F37")
        image.add_text(self.provider, 870, 400, 45)
        image.update_colors("#ffffff")


# USER_NAME = "andrey_ivanov_98"
# PHOTO_NAME = "test_photo.jpg"
# USER_ID = "1362953131"
# USER_STATUS = "Diamond"
# VPN_STATUS = False
# PROVIDER = "WireGuard"

# user_info = UserInfo()
# user_info.card(user_name=USER_NAME,
#                photo_name=PHOTO_NAME,
#                user_id=USER_ID,
#                user_status=USER_STATUS,
#                vpn_status=VPN_STATUS,
#                provider=PROVIDER)
