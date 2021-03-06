package org.reactome.server.interactors.dao;

import org.reactome.server.interactors.model.Interactor;

import java.sql.SQLException;
import java.util.List;

/**
 * @author Guilherme S Viteri <gviteri@ebi.ac.uk>
 */

public interface InteractorDAO {

    // add here something specific for Interactor
    Interactor getByAccession(String acc) throws SQLException;

    void searchByAccessions(Interactor interactorA, Interactor interactorB) throws SQLException;

    List<String> getAllAccessions() throws SQLException;

    List<Interactor> getAll() throws SQLException;

    Interactor create(Interactor interactor) throws SQLException;
}
