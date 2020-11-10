import pygame
import sys
from pygame_upgraded.fight import fight
from pygame_upgraded.winner_screen import winner_screen
from pygame_upgraded.end_screen import end_screen
from pathlib import Path

matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],
		   ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"],
		   ["Boxare Bob", "Bråkiga Berit"]]
bet_list = [["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Boxare Bob"],
			["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"], ["Boxare Bob", "Bråkiga Berit"],
			["Slaktar Sune", "Hänsynslöse Hannes"]]
bet_names_list = [["Berit", "Hannes"], ["Sune", "Bob"],
			["Bob", "Hannes"], ["Sune", "Berit"], ["Bob", "Berit"],
			["Sune", "Hannes"]]

r = Path("fighting_game/bets.txt")


# specifying font and screen size
font = pygame.font.SysFont("Arial", 30, True)
screen = pygame.display.set_mode((800, 600))

# loading and setting dimensions for rects to betting buttons
ten = pygame.image.load("pics/10$.png")
minus_ten = pygame.image.load("pics/-10$.png")
fifty = pygame.image.load("pics/50$.png")
minus_fifty = pygame.image.load("pics/-50$.png")
ten_button = pygame.Rect(430, 250, 71, 42)
minus_ten_button = pygame.Rect(505, 250, 71, 42)
fifty_button = pygame.Rect(430, 300, 71, 42)
minus_fifty_button = pygame.Rect(505, 300, 71, 42)
ten_button_2 = pygame.Rect(630, 250, 71, 42)
minus_ten_button_2 = pygame.Rect(705, 250, 71, 42)
fifty_button_2 = pygame.Rect(630, 300, 71, 42)
minus_fifty_button_2 = pygame.Rect(705, 300, 71, 42)

# fight button
fight_sign = pygame.image.load('pics/fight_sign.png')
fight_button = pygame.Rect(250, 50, 300, 100)

# loading player heads/profile pics
sune_head = pygame.image.load("pics/head_sune.png")
bob_head = pygame.image.load("pics/head_bob.png")
berit_head = pygame.image.load("pics/head_berit.png")
hannes_head = pygame.image.load("pics/head_hannes.png")


def show_stats(score1, score2, score3, score4):
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score4}", True, (255, 255, 255)), (50, 350))


def lobby_window():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music_fight/casino_music.wav")
	pygame.mixer.music.play(-1)
	casino_bg = pygame.image.load('pics/casino.png')
	screen.blit(casino_bg, (0, 0))
	blit_heads()


def player_bars(winner):
	screen.blit(font.render(f"Previous winnner: {winner}", True, (255, 255, 255)), (100, 530))
	pygame.display.update()


def blit_heads():
	screen.blit(sune_head, (10, 200))
	screen.blit(bob_head, (10, 250))
	screen.blit(berit_head, (10, 300))
	screen.blit(hannes_head, (10, 350))


def lobby():
	pygame.init()
	pygame.mixer.init()
	running = True
	score = 100
	volume = 0.5
	current_match = 0
	better_1 = 0
	better_2 = 0
	made_bet_1 = ""
	made_bet_2 = ""
	bet_counter = 1
	score_player1 = score
	score_player2 = score
	score_player3 = score
	score_player4 = score
	sune_pos = 0
	bob_pos = 0
	berit_pos = 0
	hannes_pos = 0
	lobby_window()
	show_stats(score_player1, score_player2, score_player3, score_player4)
	while running:
		minus, mute, plus = volume_buttons()
		pygame.mixer.music.set_volume(volume)
		if current_match > 5:
			end_screen(score_player1, score_player2, score_player3, score_player4)
			return
		show_bet_buttons(better_1, better_2, current_match)
		berit_pos, bob_pos, hannes_pos, sune_pos = bet_head_pfp(berit_pos, bob_pos, current_match, hannes_pos, sune_pos)

		head_berit_rect, head_berit_rect_1, head_bob_rect, head_bob_rect_1, head_hannes_rect, head_hannes_rect_1, head_sune_rect, head_sune_rect_1 = pfp_bet_rects(
			berit_pos, bob_pos, hannes_pos, sune_pos)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				# kollar position på musen
				mx, my = pygame.mouse.get_pos()
				# kollar vilken knapp på musen som tryckts ned
				if event.button == 1:

					better_1, made_bet_1 = bet_p1(better_1, current_match, head_berit_rect, head_bob_rect,
												  head_hannes_rect, head_sune_rect, made_bet_1, mx, my, score_player1,
												  score_player2, score_player3)
					better_2, made_bet_2 = bet_p2(better_2, current_match, head_berit_rect_1, head_bob_rect_1,
												  head_hannes_rect_1, head_sune_rect_1, made_bet_2, mx, my,
												  score_player2, score_player3, score_player4)

					# Volume buttons
					if plus.collidepoint(mx, my):
						volume += 0.1
						print("höjer")
					if minus.collidepoint(mx, my):
						volume -= 0.1
						print("sänker")
					if mute.collidepoint(mx, my):
						volume = 0
						print("mute")

					# kollar om musens position vid knapptryckningen kolliderar med playbutton
					if fight_button.collidepoint(mx, my):
						# starta en fight och få resultatet tillbaka
						winner, loser = fight(current_match)
						print("Winner is player " + str(winner))
						winner_screen(winner, loser, current_match)
						current_match += 1
						# printar score
						if winner == 1:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
						else:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
						# måla upp lobbyn igen
						lobby_window()

						score_player1, score_player2, score_player3, score_player4 = won_bet_calc(bet_counter, better_1,
																								  better_2, made_bet_1,
																								  made_bet_2,
																								  score_player1,
																								  score_player2,
																								  score_player3,
																								  score_player4, winner)
						# nollställer betting rutorna
						better_1 = 0
						better_2 = 0
						made_bet_1 = ""
						made_bet_2 = ""
						bet_counter += 1
						score_player1, score_player2, score_player3, score_player4 = show_score(score_player1,
																								score_player2,
																								score_player3,
																								score_player4, winner)

		# uppdaterar displayen
		pygame.display.update()


def won_bet_calc(bet_counter, better_1, better_2, made_bet_1, made_bet_2, score_player1, score_player2, score_player3,
				 score_player4, winner):
	# bettare berit vs hannes
	if bet_counter == 1:
		# berit
		if made_bet_1 == winner:
			score_player3 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player3 -= better_1
		# bob
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	# bettare sune vs bob
	if bet_counter == 2:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# bob
		if made_bet_2 == winner:
			score_player2 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player2 -= better_2
	# bettare bob vs hannes
	if bet_counter == 3:
		# bob
		if made_bet_1 == winner:
			score_player2 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player2 -= better_1
		# hannes
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	# bettare sune vs berit
	if bet_counter == 4:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# berit
		if made_bet_2 == winner:
			score_player3 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player3 -= better_2
	# bettare bob vs berit
	if bet_counter == 5:
		# bob
		if made_bet_1 == winner:
			score_player2 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player2 -= better_1
		# berit
		if made_bet_2 == winner:
			score_player3 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player3 -= better_2
	# bettare sune vs hannes
	if bet_counter == 6:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# hannes
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	return score_player1, score_player2, score_player3, score_player4


def pfp_bet_rects(berit_pos, bob_pos, hannes_pos, sune_pos):
	head_sune_rect = pygame.Rect(390, sune_pos, 40, 35)
	head_bob_rect = pygame.Rect(390, bob_pos, 40, 35)
	head_berit_rect = pygame.Rect(390, berit_pos, 40, 35)
	head_hannes_rect = pygame.Rect(390, hannes_pos, 40, 35)
	head_sune_rect_1 = pygame.Rect(590, sune_pos, 40, 35)
	head_bob_rect_1 = pygame.Rect(590, bob_pos, 40, 35)
	head_berit_rect_1 = pygame.Rect(590, berit_pos, 40, 35)
	head_hannes_rect_1 = pygame.Rect(590, hannes_pos, 40, 35)
	return head_berit_rect, head_berit_rect_1, head_bob_rect, head_bob_rect_1, head_hannes_rect, head_hannes_rect_1, head_sune_rect, head_sune_rect_1


def bet_head_pfp(berit_pos, bob_pos, current_match, hannes_pos, sune_pos):
	if current_match == 0:
		sune_pos = 250
		bob_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(bob_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(bob_head, (590, 300))
	if current_match == 1:
		berit_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(berit_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(berit_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
	if current_match == 2:
		sune_pos = 250
		berit_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	if current_match == 3:
		bob_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
	if current_match == 4:
		sune_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
		bob_pos = 250
		berit_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	if current_match == 5:
		bob_pos = 250
		berit_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	return berit_pos, bob_pos, hannes_pos, sune_pos


def bet_p2(better_2, current_match, head_berit_rect_1, head_bob_rect_1, head_hannes_rect_1, head_sune_rect_1,
		   made_bet_2, mx, my, score_player2, score_player3, score_player4):
	# player 2 bet
	if ten_button_2.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_2 >= score_player3:
				better_2 = score_player3
			else:
				better_2 += 10
		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			if better_2 >= score_player4:
				better_2 = score_player4
			else:
				better_2 += 10
		if bet_list[current_match][0] == "Boxare Bob":
			if better_2 >= score_player2:
				better_2 = score_player2
			else:
				better_2 += 10
	if minus_ten_button_2.collidepoint(mx, my):
		if bet_list[current_match][1] == "Hänsynslöse Hannes":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 10
		if bet_list[current_match][1] == "Boxare Bob":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 10
		if bet_list[current_match][1] == "Bråkiga Berit":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 10
		print('hit')
		print(better_2)
	if fifty_button_2.collidepoint(mx, my):
		if bet_list[current_match][1] == "Hänsynslöse Hannes":
			if better_2 >= score_player4:
				better_2 = score_player4
			else:
				better_2 += 50
		if bet_list[current_match][1] == "Boxare Bob":
			if better_2 >= score_player2:
				better_2 = score_player2
			else:
				better_2 += 50
		if bet_list[current_match][1] == "Bråkiga Berit":
			if better_2 >= score_player3:
				better_2 = score_player3
			else:
				better_2 += 50
	if minus_fifty_button_2.collidepoint(mx, my):
		if bet_list[current_match][1] == "Hänsynslöse Hannes":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 50
		if bet_list[current_match][1] == "Boxare Bob":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 50
		if bet_list[current_match][1] == "Bråkiga Berit":
			if better_2 <= 0:
				better_2 = 0
			else:
				better_2 -= 50
		print('hit')
		print(better_2)
	# bestämmer vilken fighter som spelare 2 väljer att betta på
	# om spelaren bettar på sune
	if head_sune_rect_1.collidepoint(mx, my):
		if bet_list[current_match][1] == "Slaktar Sune":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][1] == "Boxare Bob":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][1] == "Bråkiga Berit":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][1] == "Hänsynslöse Hannes":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

	# om spelaren bettar på Bob
	if head_bob_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

	# om spelaren bettar på Berit
	if head_berit_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

	# om spelaren bettar på Hannes
	if head_hannes_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

	return better_2, made_bet_2


def bet_p1(better_1, current_match, head_berit_rect, head_bob_rect, head_hannes_rect, head_sune_rect, made_bet_1, mx,
		   my, score_player1, score_player2, score_player3):
	# player 1 bet
	if ten_button.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_1 >= score_player3:
				better_1 = score_player3
			else:
				better_1 += 10
		if bet_list[current_match][0] == "Slaktar Sune":
			if better_1 >= score_player1:
				better_1 = score_player1
			else:
				better_1 += 10
		if bet_list[current_match][0] == "Boxare Bob":
			if better_1 >= score_player2:
				better_1 = score_player2
			else:
				better_1 += 10
	if fifty_button.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_1 >= score_player3:
				better_1 = score_player3
			else:
				better_1 += 50
		if bet_list[current_match][0] == "Slaktar Sune":
			if better_1 >= score_player1:
				better_1 = score_player1
			else:
				better_1 += 50
		if bet_list[current_match][0] == "Boxare Bob":
			if better_1 >= score_player2:
				better_1 = score_player2
			else:
				better_1 += 50
		print('hit')
		print(better_1)

		print('hit')
		print(better_1)
	if minus_ten_button.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 10
		if bet_list[current_match][0] == "Slaktar Sune":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 10
		if bet_list[current_match][0] == "Boxare Bob":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 10
		print('hit')
		print(better_1)
	if minus_fifty_button.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 50
		if bet_list[current_match][0] == "Slaktar Sune":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 50
		if bet_list[current_match][0] == "Boxare Bob":
			if better_1 <= 0:
				better_1 = 0
			else:
				better_1 -= 50
		print('hit')
		print(better_1)
	# bestämmer vilken fighter som spelare 1 väljer att betta på
	# om spelaren bettar på Sune
	if head_sune_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

	# om spelaren bettar på Bob
	if head_bob_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

	# om spelaren bettar på Berit
	if head_berit_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

	# om spelaren bettar på Hannes
	if head_hannes_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

	return better_1, made_bet_1


def show_bet_buttons(better_1, better_2, current_match):
	screen.blit(
		font.render(f"Next match:{matchup[current_match][0]} vs {matchup[current_match][1]} ", True, (255, 255, 255)),
		(50, 550))
	# betting ruta
	screen.blit(font.render("Betters:", True, (255, 255, 255)), (430, 150))
	screen.blit(font.render(f"{bet_names_list[current_match][0]}", True, (255, 255, 255)),
				(430, 200))
	screen.blit(font.render(f"{bet_names_list[current_match][1]}", True, (255, 255, 255)),
				(630, 200))
	# bets 1
	pygame.draw.rect(screen, (0, 0, 0), ten_button)
	pygame.draw.rect(screen, (0, 0, 0), minus_ten_button)
	pygame.draw.rect(screen, (0, 0, 0), fifty_button)
	pygame.draw.rect(screen, (0, 0, 0), minus_fifty_button)
	screen.blit(ten, (430, 250))
	screen.blit(minus_ten, (505, 250))
	screen.blit(fifty, (430, 300))
	screen.blit(minus_fifty, (505, 300))
	# bets 2
	pygame.draw.rect(screen, (0, 0, 0), ten_button_2)
	pygame.draw.rect(screen, (0, 0, 0), minus_ten_button_2)
	pygame.draw.rect(screen, (0, 0, 0), fifty_button_2)
	pygame.draw.rect(screen, (0, 0, 0), minus_fifty_button_2)
	screen.blit(ten, (630, 250))
	screen.blit(minus_ten, (705, 250))
	screen.blit(fifty, (630, 300))
	screen.blit(minus_fifty, (705, 300))
	# total rects
	total1 = pygame.Rect(430, 350, 146, 50)
	pygame.draw.rect(screen, (0, 0, 0), total1)
	total2 = pygame.Rect(630, 350, 146, 50)
	pygame.draw.rect(screen, (0, 0, 0), total2)
	screen.blit(font.render(f"{better_1}", True, (255, 255, 255)), (445, 360))
	screen.blit(font.render(f"{better_2}", True, (255, 255, 255)), (645, 360))
	# confirm rects
	black_bg_rect = pygame.Rect(430, 405, 146, 50)
	pygame.draw.rect(screen, (0, 0, 0), black_bg_rect)
	black_bg_rect2 = pygame.Rect(630, 405, 146, 50)
	pygame.draw.rect(screen, (0, 0, 0), black_bg_rect2)
	screen.blit(font.render(f"{better_1 * 2}", True, (255, 255, 255)), (445, 410))
	screen.blit(font.render(f"{better_2 * 2}", True, (255, 255, 255)), (645, 410))


def volume_buttons():
	screen.blit(font.render(f"MUSIC: ", True, (255, 255, 255)), (590, 10))
	plus = screen.blit(font.render(f"+", True, (255, 255, 255)), (700, 10))
	minus = screen.blit(font.render(f"-", True, (255, 255, 255)), (730, 9))
	mute = screen.blit(font.render(f"Mute", True, (255, 255, 255)), (700, 40))
	return minus, mute, plus


def show_score(score_player1, score_player2, score_player3, score_player4, winner):
	score_player1, score_player2, score_player3, score_player4 = winner_points(score_player1, score_player2,
																			   score_player3, score_player4, winner)
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score_player1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score_player2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score_player3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score_player4}", True, (255, 255, 255)), (50, 350))
	return score_player1, score_player2, score_player3, score_player4


def winner_points(score_player1, score_player2, score_player3, score_player4, winner):
	if winner == "Slaktar Sune":
		score_player1 += 100
	if winner == "Boxare Bob":
		score_player2 += 100
	if winner == "Bråkiga Berit":
		score_player3 += 100
	if winner == "Hänsynslöse Hannes":
		score_player4 += 100
	return score_player1, score_player2, score_player3, score_player4
