# Check for all events
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print('Quitting...')
        pygame.quit()  # Close Window
        quit()  # end pygame