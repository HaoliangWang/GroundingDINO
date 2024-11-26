from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2

model = load_model("groundingdino/config/GroundingDINO_SwinT_OGC.py", "weights/groundingdino_swint_ogc.pth")
IMAGE_PATH = "/home/haoliangwang/uncos/haoliang/pilot_dominoes_0mid_d3chairs_o1plants_tdwroom_0001_masks_0.png"
TEXT_PROMPT = "cuboid . chair . sphere. cone . ring ."
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25
# BOX_TRESHOLD = 0
# TEXT_TRESHOLD = 0

image_source, image = load_image(IMAGE_PATH)

boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=BOX_TRESHOLD,
    text_threshold=TEXT_TRESHOLD
)
print(logits, phrases)

annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
cv2.imwrite("annotated_image.jpg", annotated_frame)