import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter


class BarcodeGeneratorApp:

    def __init__(self, root):

        self.root = root

        self.root.title("条形码生成器")

        # 输入标签和文本框

        self.label = tk.Label(root, text="请输入条形码数据（数字）:")
        self.label.pack(pady=10)
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # 生成按钮

        self.generate_button = tk.Button(root, text="生成条形码", command=self.generate_barcode)
        self.generate_button.pack(pady=10)

        # 用于显示条形码的标签

        self.barcode_label = tk.Label(root)
        self.barcode_label.pack(pady=10)

        # 初始化条形码图像为None

        self.barcode_image = None

    def generate_barcode(self):

        # 从输入框获取数据

        data = self.entry.get()

        # 检查数据是否为空

        if not data:
            messagebox.showerror("错误", "请输入条形码数据！")
            return

            # 尝试生成条形码

        try:

            # 这里我们使用ean13作为示例，但你可以根据需要更改

            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(data, writer=ImageWriter())

            # 保存条形码到内存中的字节流

            from io import BytesIO

            buffer = BytesIO()
            ean.save(buffer, format='PNG')
            buffer.seek(0)

            # 将字节流转换为PIL图像

            self.barcode_image = Image.open(buffer)

            # 将PIL图像转换为Tkinter图像

            tk_image = ImageTk.PhotoImage(self.barcode_image)

            # 更新条形码标签以显示新图像

            self.barcode_label.config(image=tk_image)
            self.barcode_label.image = tk_image  # 保持对图像的引用

            # 可选：提供保存条形码的选项
            # save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            # if save_path:
            #     self.barcode_image.save(save_path)
            #     messagebox.showinfo("成功", f"条形码已保存到 {save_path}")

        except barcode.writer.WriterException as e:

            messagebox.showerror("条形码生成失败", f"错误: {e}")

        except Exception as e:

            messagebox.showerror("错误", f"发生未知错误: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()
