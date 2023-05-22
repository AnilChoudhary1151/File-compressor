import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
from huffman import Huffmancode

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=382
        height=379
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_64=tk.Label(root)
        GLabel_64["bg"] = "#aae1f9"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_64["font"] = ft
        GLabel_64["fg"] = "#333333"
        GLabel_64["justify"] = "center"
        GLabel_64["text"] = ""
        GLabel_64.place(x=0,y=0,width=382,height=376)

        GLabel_352=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_352["font"] = ft
        GLabel_352["fg"] = "#333333"
        GLabel_352["justify"] = "center"
        GLabel_352["text"] = "FILE COMPRESSOR"
        GLabel_352.place(x=40,y=40,width=274,height=30)

        self.compress_button=tk.Button(root)
        self.compress_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        self.compress_button["font"] = ft
        self.compress_button["fg"] = "#000000"
        self.compress_button["justify"] = "center"
        self.compress_button["text"] = "Compress"
        self.compress_button.place(x=110,y=120,width=140,height=30)
        self.compress_button["command"] = self.compress_button_command

        self.decompress_button=tk.Button(root)
        self.decompress_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        self.decompress_button["font"] = ft
        self.decompress_button["fg"] = "#000000"
        self.decompress_button["justify"] = "center"
        self.decompress_button["text"] = "Decompress"
        self.decompress_button.place(x=110,y=180,width=143,height=30)
        self.decompress_button["command"] = self.decompress_button_command

        self.reset_button=tk.Button(root)
        self.reset_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        self.reset_button["font"] = ft
        self.reset_button["fg"] = "#000000"
        self.reset_button["justify"] = "center"
        self.reset_button["text"] = "Reset"
        self.reset_button.place(x=110,y=240,width=141,height=30)
        self.reset_button["command"] = self.reset_button_command

        self.exit_button=tk.Button(root)
        self.exit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        self.exit_button["font"] = ft
        self.exit_button["fg"] = "#000000"
        self.exit_button["justify"] = "center"
        self.exit_button["text"] = "Exit"
        self.exit_button.place(x=110,y=300,width=143,height=30)
        self.exit_button["command"] = self.exit_button_command

        about_button=tk.Button(root)
        about_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=8)
        about_button["font"] = ft
        about_button["fg"] = "#000000"
        about_button["justify"] = "center"
        about_button["text"] = "i"
        about_button.place(x=350,y=340,width=30,height=30)
        about_button["command"] = self.about_button_command

    def compress_button_command(self):
        self.compress_button.config(state="disable")
        self.decompress_button.config(state="disable")
        input_file_path = filedialog.askopenfilename()
        try:
            if input_file_path:
                h = Huffmancode(input_file_path)
                output_file_path = h.compression()
                original_size = os.path.getsize(input_file_path)
                compressed_size = os.path.getsize(output_file_path)
                compression_ratio = (float(compressed_size) / float(original_size))*100 
                message = f"Compression complete!\nOriginal size: {original_size} bytes\nCompressed size: {compressed_size} bytes\nCompression percentage: {compression_ratio:.2f}"
                messagebox.showinfo("Compression Result", message)
            else:
                    messagebox.showinfo("No file selected", "Please select a file to compress.")
        except:
            messagebox.showinfo("Unable to compress", "An error occurred while compressing the file.")
  
            


    def decompress_button_command(self):
        self.compress_button.config(state="disable")
        self.decompress_button.config(state="disable")
        input_folder_path = filedialog.askdirectory()
        try:
            if input_folder_path:
                h = Huffmancode(input_folder_path)
                output_folder_path = h.decompress()
                original_size = os.path.getsize(input_folder_path+'/data.bin')
                compressed_size = os.path.getsize(output_folder_path)
                compression_ratio = (float(original_size) / float(compressed_size))*100 
                message = f"Decompression complete!\nOriginal size: {original_size} bytes\nDecompressed size: {compressed_size} bytes\nCompression percentage: {compression_ratio:.2f}"
                messagebox.showinfo("Decompression Result", message)
            else:
                messagebox.showinfo("No folder selected", "Please select a folder to decompress.")
        except:
            messagebox.showinfo("Unable to decompress", "An error occurred while decompressing the file.")
            


    def reset_button_command(self):
        self.compress_button.config(state="normal")
        self.decompress_button.config(state="normal")



    def exit_button_command(self):
        root.destroy()


    def about_button_command(self):
        tk.messagebox.showinfo("About", "File Compressor using Huffman Coding\n--------------Created By----------------\nAnil Choudhary\nAnom Chakma")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
