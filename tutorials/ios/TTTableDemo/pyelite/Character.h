//
//  Character.h
//  Three20Test
//
//  Created by Ray Wenderlich on 3/9/10.
//  Copyright 2010 Ray Wenderlich. All rights reserved.
//

#import <Foundation/Foundation.h>

typedef enum {
    kRPGClassFighter,
    kRPGClassRogue,
    kRPGClassWizard
} RPGClass;

@interface Character : NSObject {
    NSString *_name;
    int _level;
    int _xp;
    RPGClass _rpgClass;
}

@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) int level;
@property (nonatomic, assign) int xp;
@property (nonatomic, assign) RPGClass rpgClass;

- (id)initWithName:(NSString *)name level:(int)level xp:(int)xp rpgClass:(RPGClass)rpgClass;
- (NSString *)rpgClassName;
+ (NSArray *)sharedRpgClassNames;

@end
