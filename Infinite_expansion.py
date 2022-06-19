import cv2
import numpy as np
from utils.img_tools import ImgTools


class InfiniteExpansion:
    @staticmethod
    def _mouse_handler_clear_code(event, x, y, flags, data):
        # 單純點擊左鍵也會有設置點
        if event == cv2.EVENT_LBUTTONDOWN:
            # 標記點位置
            # cv2.circle(data['img'], (x, y), 3, (0, 0, 255), 3, 3)
            data['img'][y:y + IMG_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:, :]
            # 改變顯示 window 的內容
            cv2.imshow("Infinite Expansion Windows", data['img'])
            # 顯示 (x,y) 並儲存到 list中
            print(f"get points: (x, y) = ({x}, {y})")
            data['points'].append((x, y))
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            # 點擊左鍵拖曳繪製移動線段
            data['img'][y:y + IMG_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:, :]
            # 改變顯示 window 的內容
            cv2.imshow("Infinite Expansion Windows", data['img'])
            # 顯示 (x,y) 並儲存到 list中
            print(f"get points: (x, y) = ({x}, {y})")
            data['points'].append((x, y))

    @staticmethod
    def mouse_handler(event, x, y, flags, data):
        # 單純點擊左鍵也會有設置點
        if event == cv2.EVENT_LBUTTONDOWN:
            # 標記點位置
            # cv2.circle(data['img'], (x, y), 3, (0, 0, 255), 3, 3)
            """
            if 判斷主要用於判斷是否超出邊界，以及超出邊界後的圖像裁切處理
            少了if判斷會更簡潔，但對於一些邊界的效果可能會略有差異!
            """
            if x > SCREEN_SHAPE[0] - IMG_SHAPE[0] and y > SCREEN_SHAPE[1] - IMG_SHAPE[1]:
                end_x = (x + IMG_SHAPE[0]) - SCREEN_SHAPE[0]
                end_y = (y + IMG_SHAPE[1]) - SCREEN_SHAPE[1]
                data['img'][y:SCREEN_SHAPE[1], x:SCREEN_SHAPE[0]] = IMG[:-end_y, :-end_x]
            elif x > SCREEN_SHAPE[0] - IMG_SHAPE[0]:
                end_x = (x + IMG_SHAPE[0]) - SCREEN_SHAPE[0]
                data['img'][y:y + IMG_SHAPE[1], x:SCREEN_SHAPE[0]] = IMG[:, :-end_x]
            elif y > SCREEN_SHAPE[1] - IMG_SHAPE[1]:
                end_y = (y + IMG_SHAPE[1]) - SCREEN_SHAPE[1]
                data['img'][y:SCREEN_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:-end_y, :]
            elif x < 0 and y < 0:
                end_x = (x + IMG_SHAPE[0])
                end_y = (y + IMG_SHAPE[1])
                data['img'][0:end_y, 0:end_x] = IMG[-end_y:, -end_x:]
            elif x < 0:
                end_x = (x + IMG_SHAPE[0])
                data['img'][y:y + IMG_SHAPE[1], 0:end_x] = IMG[:, -end_x:]
            elif y < 0:
                end_y = (y + IMG_SHAPE[1])
                data['img'][0:end_y, x:x + IMG_SHAPE[0]] = IMG[-end_y:, :]
            else:
                data['img'][y:y + IMG_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:, :]
            # 改變顯示 window 的內容
            cv2.imshow("Infinite Expansion Windows", data['img'])
            # 顯示 (x,y) 並儲存到 list中
            print(f"get points: (x, y) = ({x}, {y})")
            data['points'].append((x, y))
        # 點擊左鍵拖曳繪製移動線段
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            # 標記點位置
            # cv2.circle(data['img'], (x, y), 3, (0, 0, 255), 3, 3)
            if x > SCREEN_SHAPE[0] - IMG_SHAPE[0] and y > SCREEN_SHAPE[1] - IMG_SHAPE[1]:
                end_x = (x + IMG_SHAPE[0]) - SCREEN_SHAPE[0]
                end_y = (y + IMG_SHAPE[1]) - SCREEN_SHAPE[1]
                data['img'][y:SCREEN_SHAPE[1], x:SCREEN_SHAPE[0]] = IMG[:-end_y, :-end_x]
            elif x > SCREEN_SHAPE[0] - IMG_SHAPE[0]:
                end_x = (x + IMG_SHAPE[0]) - SCREEN_SHAPE[0]
                data['img'][y:y + IMG_SHAPE[1], x:SCREEN_SHAPE[0]] = IMG[:, :-end_x]
            elif y > SCREEN_SHAPE[1] - IMG_SHAPE[1]:
                end_y = (y + IMG_SHAPE[1]) - SCREEN_SHAPE[1]
                data['img'][y:SCREEN_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:-end_y, :]
            elif x < 0 and y < 0:
                end_x = (x + IMG_SHAPE[0])
                end_y = (y + IMG_SHAPE[1])
                data['img'][0:end_y, 0:end_x] = IMG[-end_y:, -end_x:]
            elif x < 0:
                end_x = (x + IMG_SHAPE[0])
                data['img'][y:y + IMG_SHAPE[1], 0:end_x] = IMG[:, -end_x:]
            elif y < 0:
                end_y = (y + IMG_SHAPE[1])
                data['img'][0:end_y, x:x + IMG_SHAPE[0]] = IMG[-end_y:, :]
            else:
                data['img'][y:y + IMG_SHAPE[1], x:x + IMG_SHAPE[0]] = IMG[:, :]
            # 改變顯示 window 的內容
            cv2.imshow("Infinite Expansion Windows", data['img'])
            # 顯示 (x,y) 並儲存到 list中
            print(f"get points: (x, y) = ({x}, {y})")
            data['points'].append((x, y))

    @staticmethod
    def ie_browser_crash(im):
        # 建立 data dict, img:存放圖片, points:存放點
        data = {}
        data['img'] = im.copy()
        data['points'] = []

        # 建立一個 window
        cv2.namedWindow("Infinite Expansion Windows", 0)

        # 改變 window 成為適當圖片大小
        h, w, dim = im.shape
        print(f"Img height, width: ({h}, {w})")
        cv2.resizeWindow("Infinite Expansion Windows", w, h)

        # 顯示圖片在 window 中
        cv2.imshow('Infinite Expansion Windows', im)

        # 利用滑鼠回傳值，資料皆保存於 data dict中
        cv2.setMouseCallback("Infinite Expansion Windows", InfiniteExpansion.mouse_handler, data)

        # 等待按下任意鍵，藉由 OpenCV 內建函數釋放資源
        cv2.waitKey()
        cv2.destroyAllWindows()

        # 回傳點 list和最終圖片結果
        return data['points'], data['img']


if __name__ == "__main__":
    IMG = cv2.imread("./img/ie_error_screen_joke.png")
    IMG_SHAPE = (IMG.shape[1], IMG.shape[0])
    SCREEN_SHAPE = (1920, 1080)

    background_img = np.full((SCREEN_SHAPE[1], SCREEN_SHAPE[0], 3), 255, np.uint8)  # 白色底圖
    # background_img = cv2.imread("../img/your_own_background_img.png")  # 可以放入自己的背景圖片!

    print("Click on the screen and press any key for end process")
    points, final_img = InfiniteExpansion.ie_browser_crash(background_img)

    print("\npoints list:")
    print(points)
    ImgTools.show_img(final_img)
    filename = "./img/tmp.png"
    cv2.imencode('.png', final_img)[1].tofile(filename)
