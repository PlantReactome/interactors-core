package org.reactome.server.tools.interactors.mapper;

import java.util.List;

/**
 * Maps an Entity which is the accessionA and its interactions list.
 *
 * @author Guilherme S Viteri <gviteri@ebi.ac.uk>
 */
@SuppressWarnings("unused")
public class InteractorEntity {

    private String acc;
    private Integer count;
    private List<Interactor> interactors;

    public String getAcc() {
        return acc;
    }

    public void setAcc(String acc) {
        this.acc = acc;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }

    public List<Interactor> getInteractors() {
        return interactors;
    }

    public void setInteractors(List<Interactor> interactors) {
        this.interactors = interactors;
    }
}
