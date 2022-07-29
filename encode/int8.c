/*
《计算之魂》 思考题 3.3
设计一种编码方法，用8位二进制数表示浮点数
基于 IEEE 754 float32 -> float8

author: Jack Lee
date:   July 28, 2022 

History: 
三种编码方案

方案1：
S:1, EXP:3, Fraction:4
整数部: < 2 ** 3 = 8
小数部：< 0.0001b = 0.0625

方案2：
S:1, EXP:4, Fraction:3
整数部: < 2 ** 7 = 128
小数部: < 0.001b = 0.125

方案3：
S:1, EXP:5, Fraction:2
整数部: < 2 ** 15 = 32768
小数部: < 0.01b = 0.25
*/

#include <stdio.h>
#include <string.h>

typedef unsigned char   __u8;
typedef unsigned short  __u16;
typedef unsigned int    __u32;

/* Version 1
typedef struct float8
{
    __u8    frac:4;
    __u8    exp:3;
    __u8    sign:1;
} __attribute__((packed)) FLOAT8;


typedef struct float32
{
    __u32    sign:1;
    __u32    exp:8;
    __u32    frac:23;
}__attribute__((packed)) FLOAT32;



//
// encode float to INT8
// para:
// f    - float number to be encoded
// exp_size - the number of bits to store exponent
// fraction_size - the number of bits to store fraction, which M = 1 + f
// 
// exp_size + fraction_size = 7 bits
// return:
//  the code of f follow INT8 rule 
//
FLOAT8 float32_2_int8(float f)
{
    FLOAT8 f8 = {0,0,0};
    __u32*  p = (__u32*)&f;

    // negative number, the 7th bit = 1
    if( 0x80000000 & *p )
        f8.sign = 1;

    // 取指数部
    f8.exp = (((*p) >> 23) & 0x00ff) - 127 + 3;   // 3 = 2 ** (3-1) - 1

    // 取小数部, 取高4位
    f8.frac = ((*p) & 0x007fffff) >> (23 - 4);
    
    return f8;
}


//
// decode INT8 to float 32-bit
//
float int8_2_float32(FLOAT8 f8)
{
    //FLOAT32 f32 = {0,0,0};
    __u32 decode = 0;
    __u32 tmp;
    float* f;

    f = (float*)&decode;
    // negative number, the 7th bit = 1
    if( f8.sign ) decode = 0x80000000;
    
    // 取指数部
    tmp = f8.exp - 3 + 127;
    decode |= tmp << 23;

    // 取小数部, 取高4位
    tmp = ((__u32)(f8.frac)) << (23 - 4);
    decode |= tmp;
    printf("%f, 0x%x 0x%x\n", *f, decode, tmp);
    
    return *f;
}
*/

// version 2
typedef struct float8
{
    __u8    frac:3;
    __u8    exp:4;
    __u8    sign:1;
} __attribute__((packed)) FLOAT8;


//
// encode float to INT8
// para:
// f    - float number to be encoded
// exp_size - the number of bits to store exponent
// fraction_size - the number of bits to store fraction, which M = 1 + f
// 
// exp_size + fraction_size = 7 bits
// return:
//  the code of f follow INT8 rule 
//
FLOAT8 float32_2_int8(float f)
{
    FLOAT8 f8 = {0,0,0};
    __u32*  p = (__u32*)&f;

    // negative number, the 7th bit = 1
    if( 0x80000000 & *p )
        f8.sign = 1;

    // 取指数部
    f8.exp = (((*p) >> 23) & 0x00ff) - 127 + 7;   // 3 = 2 ** (3-1) - 1

    // 取小数部, 取高3位
    f8.frac = ((*p) & 0x007fffff) >> (23 - 3);
    
    return f8;
}


//
// decode INT8 to float 32-bit
//
float int8_2_float32(FLOAT8 f8)
{
    //FLOAT32 f32 = {0,0,0};
    __u32 decode = 0;
    __u32 tmp;
    float* f;

    f = (float*)&decode;
    // negative number, the 7th bit = 1
    if( f8.sign ) decode = 0x80000000;
    
    // 取指数部
    tmp = f8.exp - 7 + 127;
    decode |= tmp << 23;

    // 取小数部, 取高3位
    tmp = ((__u32)(f8.frac)) << (23 - 3);
    decode |= tmp;
    printf("%f, 0x%x 0x%x\n", *f, decode, tmp);
    
    return *f;
}


int main()
{
    float f = -9.625;
    unsigned int i;
    unsigned int* p = (unsigned int *)&f;
    FLOAT8 f8;
    float  f32;
    __u8 *p8;

    // 输出 -9.625 的二进制编码
    printf("float size = %lu, %f, 0x%X\n", sizeof(float), f, *p);

    for( i = 0; i < (sizeof(float) * 8); i++)
    {
        if( i > 0 && (i % 4 == 0) )
            printf("    ");

        if( (0x80000000 >> i) & *p )
            printf("1 ");
        else
            printf("0 ");
    }
    printf("\n");
    
    f8 = float32_2_int8(f);
    p8 = (__u8*)&f8;
    for( i = 0; i < (sizeof(FLOAT8) * 8); i++)
    {
        if( i > 0 && (i % 4 == 0) )
            printf("    ");

        if( (0x80 >> i) & *p8 )
            printf("1 ");
        else
            printf("0 ");
    }
    printf("\n");

    f32 = int8_2_float32(f8);
    p = (__u32*)&f32;
    for( i = 0; i < (sizeof(float) * 8); i++)
    {
        if( i > 0 && (i % 4 == 0) )
            printf("    ");

        if( (0x80000000 >> i) & *p )
            printf("1 ");
        else
            printf("0 ");
    }
    printf("\n");
    
    printf("INT8 -> float %f\n", f32);

    // min-max INT8 float
    for(i = 0; i < 16; i++)
    {
        f8.sign = 0;
        f8.exp = i;
        f8.frac = 0x7;
        f32 = int8_2_float32(f8);
        p = (__u32*)&f32;
        printf(" INT8 -> float %f\n", f32);
    }

    /*
    // min-max INT8 float
    for(i = 0; i < 8; i++)
    {
        f8.sign = 0;
        f8.exp = i;
        f8.frac = 0xf;
        f32 = int8_2_float32(f8);
        p = (__u32*)&f32;
        printf(" INT8 -> float %f\n", f32);
    }
    */

    printf("\n");

    return 0;
}
