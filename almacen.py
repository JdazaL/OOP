##pseudocodigo
from random import seed


class products
{
    ### Atributos ###
    bar_code=' ' 
    name=' '
    price=' '
    elaboration_date=' '
    expiry_date=' '
    net_content=' '
    available_quantity=' '
    brand=' '
    ### Fin atributos ###

    ### Metodos ###
    change_name(newname)
    change_net_content(newnet_content)
    change_expiry_date(newexpiry_date)
    change_elaboration_date(newelaboration_date)
    change_available_quantity(newavailable_quantity)
    change_brand(newbrand)
    change_bar_code(newbar_code)
    change_price(newprice)

    see_name(name)
    see_net_content(net_content)
    see_expiry_date(expiry_date)
    see_elaboration_date(elaboration_date)
    see_available_quantity(available_quantity)
    see_brand(brand)
    see_bar_code(bar_code)
    see_price(price)

    ### Fin metodos ###
}

class worker
{
    ### Atributos ###
    id_card=' '
    name=' '
    age=' '
    schedule=' '
    restock_order=' '
    order=' '
    
    ### Fin Atributos ###

    ### Metodos ###
    
    change_id_card(newid_card)
    change_name(newname)
    change_age(newage)

    see_schedule(schedule)
    see_name(name)
    see_net_content(net_content)
    see_expiry_date(expiry_date)
    see_elaboration_date(elaboration_date)
    see_available_quantity(available_quantity)
    see_brand(brand)
    see_bar_code(bar_code)
    see_price(price)

    make_restock_order(newrestock_order)
    receive_order(order)

    ### Fin metodos ###
}

class supplier
{
    ### Atributos ###

    supplier_id=' '
    name=' '
    age=' '
    restock_order=' '

    ### Fin Atributos ###

    ### Metodos ###    

    change_supplier_id(newsupplier_id)

    receive_restock_order(restock_order)

    see_name(name)
    see_supplier_id(supplier_id)

    ### Fin metodos ###

}

class client
{
    ### Atributos ###
    id=' '
    order=' '
    age=' '
    name=' '

    ### Fin Atributos ###

    ### Metodos ###    

    change_id(newid)
    see_id(id)
    make_order(neworder)
    change_order(neworder)
    see_oder(order)
    change_name(newname)
    change_age(newage)
    ### Fin metodos ###

}