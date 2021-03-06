import coordinatedescent


def main():
    optimizer = coordinatedescent.CoordinateDescent()
    minimiser, min_value, gradient = optimizer.execute()
    result = f'''
    =====Function F(X1, X2) has a local minimum at {minimiser}=========
      - Min Value = {min_value}
      - Slope     = {gradient} 
    '''
    print(result.strip())


if __name__ == '__main__':
    main()
