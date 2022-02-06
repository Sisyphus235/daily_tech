package com.factory;


import java.util.function.Supplier;

public enum CoinType {

    private final Supplier<Coin> constructor;
}