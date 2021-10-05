#!/usr/bin/python3
# @author: Anonymous Hacks - 4anonz
import zipfile
from tqdm import tqdm

whi = "\033[1;37m"
red = "\033[1;31m"
yel = "\033[1;33m"
cya = "\033[0;36m"
res = "\033[0;37;40m"

def print_i():
	print(" ______")
	print("| ___ \ ______  _ __")
	print("| |_/ /|__  (_)| `__ \\")
	print("| ___ \  / /| || |__) |")
	print("| |_/ / / / | || -___/")
	print("\____/ /____|_|| |")
	print("               |_|")


def is_pass(zip_file, password):
	try:
		zip_file.extractall(pwd=password)
	except:
		return False
	else:
		return True


def get_input():
	zip_file = input(f"{cya}[$>]Zip file~${res} ")
	wordlist = input(f"{cya}[$>]Wordlist~${res} ")
	if not zip_file.endswith(".zip"):
		print(f"{red}[!]{whi} Error only .zip file is supported.!")
		exit(1)
	try:
		open(zip_file)
		open(wordlist)
	except FileNotFoundError:
		print(f"{red}[!]{whi} Failed to open file, Please specify a valid file.{res}")
		exit(1)
	except Exception as err:
		print(f"{red}[!]{whi}{str(err)}")
	return zip_file, wordlist


def main():
	print(cya)
	print_i()
	print(f"{yel}Author:{whi} Anonymous Hacks-4anonz")
	print(f"{yel}GitHub:{whi} https://github.com/4anonz{res}\n")
	print(f"{cya}[1]:{res} Start Attack")
	print(f"{cya}[0]:{res} Exit\n\n")
	choice = input(f"{cya}[$>]Choice~$ {res}")
	if choice != '1':
		exit(0)
	
	zip_file, wordlist = get_input()
	n_pass = len(list(open(wordlist, "rb")))
	zip_file = zipfile.ZipFile(zip_file)
	print(f"{cya}[*]{res} {n_pass} passwords loaded.!!")
	print(f"{cya}[*]{res} Hold on, trying {n_pass} passwords.")
	with open(wordlist, "rb") as passwords:
		for password in tqdm(passwords, total=n_pass, unit="pass"):
			if(is_pass(zip_file, password.strip())):
				print(f"{cya}[*]{res} Password found️: {yel}{password.decode().strip()}{res}")
				exit(0)
			else:
				continue
	print(f"{cya}[!]{res} Password not found.. Maybe try another wordlist️")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(f"\n{cya}[*]{res} Quitting.!!")
		exit(0)
